import os

from datetime import (
    datetime,
    timedelta,
    timezone
)

from dotenv import load_dotenv

from jose import (
    JWTError,
    jwt
)

from passlib.context import (
    CryptContext
)

from sqlalchemy.orm import (
    Session
)

from fastapi import (
    Depends,
    HTTPException,
    status
)

from fastapi.security import (
    OAuth2PasswordBearer
)

from app.database import (
    get_db
)

from app.models import (
    User
)


# ==========================================
# LOAD ENV
# ==========================================

load_dotenv()


# ==========================================
# JWT CONFIG
# ==========================================

SECRET_KEY = os.getenv(
    "SECRET_KEY"
)

if not SECRET_KEY:

    raise ValueError(
        "SECRET_KEY is not set"
    )

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = int(

    os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES",
        60 * 24 * 7
    )
)


# ==========================================
# PASSWORD HASHER
# ==========================================

pwd_context = CryptContext(

    schemes=["bcrypt"],

    deprecated="auto"
)


# ==========================================
# OAUTH
# ==========================================

oauth2_scheme = OAuth2PasswordBearer(

    tokenUrl="/api/auth/login"
)


# ==========================================
# PASSWORD VERIFY
# ==========================================

def verify_password(

        plain_password: str,

        hashed_password: str

) -> bool:

    return pwd_context.verify(

        plain_password,

        hashed_password
    )


# ==========================================
# PASSWORD HASH
# ==========================================

def get_password_hash(
        password: str
) -> str:

    return pwd_context.hash(
        password[:72]
    )


# ==========================================
# AUTHENTICATE USER
# ==========================================

def authenticate_user(

        db: Session,

        email: str,

        password: str
):

    normalized_email = (

        email
        .strip()
        .lower()
    )

    user = db.query(User).filter(

        User.email == normalized_email

    ).first()

    if not user:

        return None

    if not verify_password(

            password,

            user.hashed_password
    ):

        return None

    return user


# ==========================================
# CREATE ACCESS TOKEN
# ==========================================

def create_access_token(

        data: dict,

        expires_delta: timedelta = None
):

    to_encode = data.copy()

    expire = datetime.now(

        timezone.utc

    ) + (

        expires_delta

        or

        timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    to_encode.update({

        "exp": expire
    })

    encoded_jwt = jwt.encode(

        to_encode,

        SECRET_KEY,

        algorithm=ALGORITHM
    )

    return encoded_jwt


# ==========================================
# GET CURRENT USER
# ==========================================

def get_current_user(

    token: str = Depends(
        oauth2_scheme
    ),

    db: Session = Depends(
        get_db
    )
):

    credentials_exception = HTTPException(

        status_code=status.HTTP_401_UNAUTHORIZED,

        detail=(
            "Could not validate credentials"
        ),

        headers={
            "WWW-Authenticate": "Bearer"
        }
    )

    try:

        payload = jwt.decode(

            token,

            SECRET_KEY,

            algorithms=[ALGORITHM]
        )

        user_id = payload.get(
            "sub"
        )

        if user_id is None:

            raise credentials_exception

    except JWTError:

        raise credentials_exception

    user = db.query(User).filter(

        User.id == int(user_id)

    ).first()

    if user is None:

        raise credentials_exception

    return user