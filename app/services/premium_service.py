# app/services/premium_service.py


# =====================================================
# FREE / PREMIUM MATRIX ELEMENTS
# =====================================================

FREE_MATRIX_ELEMENTS = [

    "center",

    "business_card",

    "money_channel",

    "love_channel",

    "age_circle",

    "year_energies"
]


PREMIUM_MATRIX_ELEMENTS = [

    "spiritual_destiny",

    "social_destiny",

    "material_destiny",

    "male_generation_line",

    "female_generation_line",

    "karmic_tail",

    "top_inner",

    "bottom_inner",

    "left_inner",

    "right_inner",

    "diagonal_1",

    "diagonal_2",

    "geometry",

    "full_matrix_analysis"
]


# =====================================================
# TAROT LIMITS
# =====================================================

FREE_TAROT_LIMIT = 5

PREMIUM_TAROT_LIMIT = 999999


FREE_TAROT_SPREADS = [

    "daily_card",

    "yes_no",

    "future"
]


PREMIUM_TAROT_SPREADS = [

    "his_thoughts",

    "celtic_cross"
]


# =====================================================
# AI LIMITS
# =====================================================

FREE_AI_LIMIT = 5

PREMIUM_AI_LIMIT = 999999


# =====================================================
# PREMIUM CHECK
# =====================================================

def is_premium(user):

    return getattr(
        user,
        "is_premium",
        False
    )


# =====================================================
# MATRIX ACCESS
# =====================================================

def can_access_matrix_element(
        user,
        element_name
):

    if element_name in FREE_MATRIX_ELEMENTS:

        return True

    if element_name in PREMIUM_MATRIX_ELEMENTS:

        return is_premium(user)

    return False


# =====================================================
# FULL AI ACCESS
# =====================================================

def can_access_full_ai(
        is_premium_value
):

    return is_premium_value


# =====================================================
# AI QUESTIONS
# =====================================================

def can_ask_ai_question(
        is_premium_value,
        used_questions
):

    if is_premium_value:

        return True

    return used_questions < FREE_AI_LIMIT


# =====================================================
# TAROT USAGE
# =====================================================

def can_use_tarot(
        is_premium_value,
        used_spreads
):

    if is_premium_value:

        return True

    return used_spreads < FREE_TAROT_LIMIT


# =====================================================
# TAROT SPREAD ACCESS
# =====================================================

def can_access_tarot_spread(
        is_premium_value,
        spread_type
):

    if spread_type in FREE_TAROT_SPREADS:

        return True

    if spread_type in PREMIUM_TAROT_SPREADS:

        return is_premium_value

    return False


# =====================================================
# FULL MATRIX ACCESS
# =====================================================

def can_access_full_matrix(
        user
):

    return is_premium(user)


# =====================================================
# UNLIMITED AI
# =====================================================

def has_unlimited_ai(user):

    return is_premium(user)


# =====================================================
# UNLIMITED TAROT
# =====================================================

def has_unlimited_tarot(user):

    return is_premium(user)