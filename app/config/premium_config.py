# =========================================
# FREE MATRIX ELEMENTS
# =========================================

FREE_MATRIX_ELEMENTS = {

    # основные точки
    "center",

    "business_card",

    # предназначения
    "spiritual_destiny",

    "social_destiny",

    "material_destiny",

    # базовые энергии
    "year_energies",

    # стороны света
    "top",

    "bottom",

    "left",

    "right",
}


# =========================================
# PREMIUM MATRIX ELEMENTS
# =========================================

PREMIUM_MATRIX_ELEMENTS = {

    # внутренние точки
    "top_inner",

    "bottom_inner",

    "left_inner",

    "right_inner",

    # углы
    "top_left",

    "top_right",

    "bottom_left",

    "bottom_right",

    # линии рода
    "male_generation_line",

    "female_generation_line",

    # каналы
    "money_channel",

    "love_channel",

    # карма
    "karma_tail",

    # диагонали
    "diagonals",

    # квадраты
    "inner_square",

    "outer_square",
}


# =========================================
# FREE TAROT SPREADS
# =========================================

FREE_TAROT_SPREADS = {

    "daily_card",

    "yes_no",

    "his_thoughts",

    "future",
}


# =========================================
# PREMIUM TAROT SPREADS
# =========================================

PREMIUM_TAROT_SPREADS = {

    "celtic_cross",
}


# =========================================
# PREMIUM FEATURES
# =========================================

PREMIUM_FEATURES = {

    "unlimited_ai_questions",

    "full_matrix_analysis",

    "deep_element_analysis",

    "all_matrix_elements",

    "all_channels",

    "all_lines",

    "full_year_cycles",

    "premium_tarot_spreads",
}


# =========================================
# VALIDATION
# =========================================

ALL_MATRIX_ELEMENTS = (
    FREE_MATRIX_ELEMENTS |
    PREMIUM_MATRIX_ELEMENTS
)

ALL_TAROT_SPREADS = (
    FREE_TAROT_SPREADS |
    PREMIUM_TAROT_SPREADS
)


# =========================================
# HELPERS
# =========================================

def is_free_matrix_element(
        element_name
):

    return (
        element_name
        in FREE_MATRIX_ELEMENTS
    )


def is_premium_matrix_element(
        element_name
):

    return (
        element_name
        in PREMIUM_MATRIX_ELEMENTS
    )


def is_free_tarot_spread(
        spread_name
):

    return (
        spread_name
        in FREE_TAROT_SPREADS
    )


def is_premium_tarot_spread(
        spread_name
):

    return (
        spread_name
        in PREMIUM_TAROT_SPREADS
    )