# app/services/matrix_interpreter.py

from app.data.arcana_meanings import ARCANA


# =====================================================
# ПОЛУЧИТЬ АРКАН
# =====================================================

def get_arcana_info(arcana_number: int):

    return ARCANA.get(
        arcana_number,
        {
            "name": "Неизвестный аркан",
            "short": "",
            "light": "",
            "shadow": "",
            "mission": "",
            "love": "",
            "money": ""
        }
    )


# =====================================================
# СОЗДАНИЕ РАЗБОРА АРКАНА
# =====================================================

def build_arcana_reading(arcana):

    info = get_arcana_info(arcana)

    return {

        "arcana": arcana,

        "name": info["name"],

        "short": info["short"],

        "light": info["light"],

        "shadow": info["shadow"],

        "mission": info["mission"],

        "love": info["love"],

        "money": info["money"]
    }


# =====================================================
# ЦЕНТР
# =====================================================

def interpret_center(matrix):

    return {

        "position": "center",

        **build_arcana_reading(
            matrix["center"]
        )
    }


# =====================================================
# ВИЗИТКА
# =====================================================

def interpret_business_card(matrix):

    return {

        "position": "business_card",

        **build_arcana_reading(
            matrix["business_card"]
        )
    }


# =====================================================
# ДЕНЕЖНЫЙ КАНАЛ
# =====================================================

def interpret_money_channel(matrix):

    channel = []

    for arcana in matrix["money_channel"]:

        channel.append(
            build_arcana_reading(arcana)
        )

    return {

        "position": "money_channel",

        "channel": channel,

        "strong_energies":
            matrix["strong_money_energies"],

        "weak_energies":
            matrix["weak_money_energies"],

        "summary":
            "Финансовая реализация, "
            "способ заработка и денежные блоки."
    }


# =====================================================
# ЛЮБОВНЫЙ КАНАЛ
# =====================================================

def interpret_love_channel(matrix):

    channel = []

    for arcana in matrix["love_channel"]:

        channel.append(
            build_arcana_reading(arcana)
        )

    return {

        "position": "love_channel",

        "channel": channel,

        "harmonious":
            matrix["harmonious_energies"],

        "problematic":
            matrix["problematic_energies"],

        "summary":
            "Эмоциональная реализация "
            "и отношения."
    }


# =====================================================
# ПРЕДНАЗНАЧЕНИЯ
# =====================================================

def interpret_destinies(matrix):

    return {

        "spiritual_destiny":
            build_arcana_reading(
                matrix["spiritual_destiny"]
            ),

        "social_destiny":
            build_arcana_reading(
                matrix["social_destiny"]
            ),

        "material_destiny":
            build_arcana_reading(
                matrix["material_destiny"]
            )
    }


# =====================================================
# РОДОВЫЕ ЛИНИИ
# =====================================================

def interpret_generation_lines(matrix):

    male = []
    female = []

    for arcana in matrix["male_generation_line"]:

        male.append(
            build_arcana_reading(arcana)
        )

    for arcana in matrix["female_generation_line"]:

        female.append(
            build_arcana_reading(arcana)
        )

    return {

        "male_generation_line": male,

        "female_generation_line": female
    }


# =====================================================
# КАРМИЧЕСКИЙ ХВОСТ
# =====================================================

def interpret_karmic_tail(matrix):

    karmic = []

    for arcana in matrix["karmic_tail"]:

        karmic.append(
            build_arcana_reading(arcana)
        )

    return {

        "karmic_tail": karmic,

        "summary":
            "Кармические уроки "
            "и повторяющиеся сценарии."
    }


# =====================================================
# ВНУТРЕННИЕ ТОЧКИ
# =====================================================

def interpret_inner_points(matrix):

    return {

        "top_inner":
            build_arcana_reading(
                matrix["top_inner"]
            ),

        "bottom_inner":
            build_arcana_reading(
                matrix["bottom_inner"]
            ),

        "left_inner":
            build_arcana_reading(
                matrix["left_inner"]
            ),

        "right_inner":
            build_arcana_reading(
                matrix["right_inner"]
            ),

        "diagonal_1":
            build_arcana_reading(
                matrix["diagonal_1"]
            ),

        "diagonal_2":
            build_arcana_reading(
                matrix["diagonal_2"]
            )
    }


# =====================================================
# ВОЗРАСТНОЙ КРУГ
# =====================================================

def interpret_age_circle(matrix):

    result = []

    for item in matrix["age_circle"]:

        arcana_data = build_arcana_reading(
            item["arcana"]
        )

        result.append({

            "age": item["age"],

            **arcana_data
        })

    return result


# =====================================================
# РАЗБОР ОТДЕЛЬНОГО ЭЛЕМЕНТА
# =====================================================

def interpret_matrix_element(
        matrix,
        element_name
):

    element_map = {

        "center":
            matrix["center"],

        "business_card":
            matrix["business_card"],

        "spiritual_destiny":
            matrix["spiritual_destiny"],

        "social_destiny":
            matrix["social_destiny"],

        "material_destiny":
            matrix["material_destiny"],

        "top_inner":
            matrix["top_inner"],

        "bottom_inner":
            matrix["bottom_inner"],

        "left_inner":
            matrix["left_inner"],

        "right_inner":
            matrix["right_inner"],

        "diagonal_1":
            matrix["diagonal_1"],

        "diagonal_2":
            matrix["diagonal_2"],
    }

    if element_name not in element_map:

        return {

            "error":
                "Element not found"
        }

    arcana = element_map[element_name]

    return {

        "element": element_name,

        **build_arcana_reading(arcana)
    }


# =====================================================
# ПОЛНЫЙ РАЗБОР
# =====================================================

def generate_full_matrix_reading(matrix):

    return {

        "center":
            interpret_center(matrix),

        "business_card":
            interpret_business_card(matrix),

        "money_channel":
            interpret_money_channel(matrix),

        "love_channel":
            interpret_love_channel(matrix),

        "destinies":
            interpret_destinies(matrix),

        "generation_lines":
            interpret_generation_lines(matrix),

        "karmic_tail":
            interpret_karmic_tail(matrix),

        "inner_points":
            interpret_inner_points(matrix),

        "age_circle":
            interpret_age_circle(matrix)
    }