FREE_TAROT_LIMIT = 5

FREE_AI_LIMIT = 10


FREE_ELEMENTS = [

    "center",

    "money_channel",

    "love_channel",

    "year_energies"
]


PREMIUM_ELEMENTS = [

    "karmic_tail",

    "male_generation_line",

    "female_generation_line",

    "spiritual_destiny",

    "social_destiny",

    "material_destiny"
]


def can_use_ai(user):

    if user.is_premium:
        return True

    return user.ai_questions_used < FREE_AI_LIMIT


def can_use_tarot(user):

    if user.is_premium:
        return True

    return (
        user.tarot_spreads_used <
        FREE_TAROT_LIMIT
    )


def can_access_element(
        user,
        element
):

    if user.is_premium:
        return True

    return element in FREE_ELEMENTS