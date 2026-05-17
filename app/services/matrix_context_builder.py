# ==========================================
# SAFE FORMATTERS
# ==========================================

def format_value(value):

    if value is None:
        return "Не указано"

    if isinstance(value, list):

        if not value:
            return "Не указано"

        return ", ".join(
            str(item)
            for item in value
        )

    if isinstance(value, dict):

        if not value:
            return "Не указано"

        result = []

        for key, item in value.items():

            result.append(
                f"{key}: {item}"
            )

        return ", ".join(result)

    return str(value)


# ==========================================
# MATRIX CONTEXT BUILDER
# ==========================================

def build_matrix_context(matrix):
    """
    Формирует текстовый контекст матрицы
    для AI анализа
    """

    if not isinstance(matrix, dict):

        raise ValueError(
            "matrix must be dict"
        )

    sections = [

        (
            "ЦЕНТР",
            matrix.get("center")
        ),

        (
            "ВИЗИТКА",
            matrix.get("business_card")
        ),

        (
            "ДУХОВНОЕ ПРЕДНАЗНАЧЕНИЕ",
            matrix.get("spiritual_destiny")
        ),

        (
            "СОЦИАЛЬНОЕ ПРЕДНАЗНАЧЕНИЕ",
            matrix.get("social_destiny")
        ),

        (
            "МАТЕРИАЛЬНОЕ ПРЕДНАЗНАЧЕНИЕ",
            matrix.get("material_destiny")
        ),

        (
            "КАРМИЧЕСКИЙ ХВОСТ",
            matrix.get("karma_tail")
        ),

        (
            "ДЕНЕЖНЫЙ КАНАЛ",
            matrix.get("money_channel")
        ),

        (
            "ЛЮБОВНЫЙ КАНАЛ",
            matrix.get("love_channel")
        ),

        (
            "МУЖСКОЙ РОД",
            matrix.get("male_generation_line")
        ),

        (
            "ЖЕНСКИЙ РОД",
            matrix.get("female_generation_line")
        ),

        (
            "ВНУТРЕННИЕ ТОЧКИ",
            matrix.get("inner_points")
        )
    ]

    result = []

    for title, value in sections:

        result.append(
            f"""
{title}:
{format_value(value)}
"""
        )

    return "\n".join(result)