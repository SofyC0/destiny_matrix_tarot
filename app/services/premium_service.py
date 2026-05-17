from app.config.premium_config import (
    FREE_MATRIX_ELEMENTS,
    PREMIUM_MATRIX_ELEMENTS
)


# =========================================
# PREMIUM CHECK
# =========================================

def is_premium(user):

    return getattr(user, "is_premium", False)


# =========================================
# ДОСТУП К ЭЛЕМЕНТУ
# =========================================

def can_access_matrix_element(
        user,
        element_name
):

    # бесплатные
    if element_name in FREE_MATRIX_ELEMENTS:
        return True

    # premium
    if element_name in PREMIUM_MATRIX_ELEMENTS:

        return is_premium(user)

    return False


# =========================================
# AI ВОПРОСЫ
# =========================================

def can_ask_ai_question(user):

    return is_premium(user)