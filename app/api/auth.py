from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session

from app.database import (
    get_db
)

from app.models import (
    User
)

from app.schemas import (
    UserCreate,
    UserLogin
)

from app.api.auth_utils import (

    get_password_hash,

    verify_password,

    create_access_token
)

from app.services.matrix_service import (
    calculate_full_matrix
)


router = APIRouter()


# ==========================================
# HELPERS
# ==========================================

def normalize_email(
        email: str
):

    return (
        email
        .strip()
        .lower()
    )


def normalize_username(
        username: str
):

    return (
        username
        .strip()
    )


# ==========================================
# REGISTER
# ==========================================

@router.post("/register")
def register(

        user: UserCreate,

        db: Session = Depends(get_db)
):

    # normalize
    email = normalize_email(
        user.email
    )

    username = normalize_username(
        user.username
    )

    # ==========================================
    # EMAIL EXISTS
    # ==========================================

    existing_email = db.query(User).filter(

        User.email == email

    ).first()

    if existing_email:

        raise HTTPException(

            status_code=status.HTTP_400_BAD_REQUEST,

            detail=(
                "Email already registered"
            )
        )

    # ==========================================
    # USERNAME EXISTS
    # ==========================================

    existing_username = db.query(User).filter(

        User.username == username

    ).first()

    if existing_username:

        raise HTTPException(

            status_code=status.HTTP_400_BAD_REQUEST,

            detail=(
                "Username already taken"
            )
        )

    # ==========================================
    # PASSWORD HASH
    # ==========================================

    hashed_password = get_password_hash(

        user.password[:72]
    )

    # ==========================================
    # MATRIX CALCULATION
    # ==========================================

    matrix_data = calculate_full_matrix(

        day=user.birth_day,

        month=user.birth_month,

        year=user.birth_year
    )

    # ==========================================
    # CREATE USER
    # ==========================================

    new_user = User(

        email=email,

        username=username,

        hashed_password=hashed_password,

        birth_day=user.birth_day,

        birth_month=user.birth_month,

        birth_year=user.birth_year,

        matrix_data=matrix_data,

        is_premium=False
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    # ==========================================
    # AUTO LOGIN
    # ==========================================

    access_token = create_access_token(

        data={
            "sub": str(new_user.id)
        }
    )

    return {

        "message": (
            "User created successfully"
        ),

        "access_token": access_token,

        "token_type": "bearer",

        "user": {

            "id": new_user.id,

            "email": new_user.email,

            "username": new_user.username,

            "is_premium": (
                new_user.is_premium
            )
        },

        "matrix": matrix_data
    }


# ==========================================
# LOGIN
# ==========================================

@router.post("/login")
def login(

        user: UserLogin,

        db: Session = Depends(get_db)
):

    email = normalize_email(
        user.email
    )

    db_user = db.query(User).filter(

        User.email == email

    ).first()

    # ==========================================
    # INVALID EMAIL
    # ==========================================

    if not db_user:

        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Invalid credentials"
        )

    # ==========================================
    # INVALID PASSWORD
    # ==========================================

    if not verify_password(

            user.password,

            db_user.hashed_password
    ):

        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Invalid credentials"
        )

    # ==========================================
    # ACCESS TOKEN
    # ==========================================

    access_token = create_access_token(

        data={
            "sub": str(db_user.id)
        }
    )

    return {

        "access_token": access_token,

        "token_type": "bearer",

        "user": {

            "id": db_user.id,

            "email": db_user.email,

            "username": db_user.username,

            "is_premium": (
                db_user.is_premium
            )
        }
    }