# app/services/matrix_interpreter.py

from app.data.arcana_meanings import ARCANA


# ======================================================
# ПОЛУЧИТЬ ИНФО ОБ АРКАНЕ
# ======================================================

def get_arcana_info(arcana_number: int):

    return ARCANA.get(

        arcana_number,

        {
            "name": "Неизвестно",
            "short": "",
            "light": "",
            "shadow": ""
        }
    )


# ======================================================
# ЦЕНТР МАТРИЦЫ
# ======================================================

def interpret_center(matrix):

    center = matrix["main_arcana"]["center"]

    info = get_arcana_info(center)

    return {

        "position": "center",

        "arcana": center,

        "name": info["name"],

        "meaning": {

            "short": info["short"],

            "light": info["light"],

            "shadow": info["shadow"],

            "mission": info["mission"],

            "love": info["love"],

            "money": info["money"]
        }
    }


# ======================================================
# ВИЗИТКА
# ======================================================

def interpret_business_card(matrix):

    arcana = matrix["business_card"]

    info = get_arcana_info(arcana)

    return {

        "position": "business_card",

        "arcana": arcana,

        "name": info["name"],

        "meaning": {

            "short": info["short"],

            "light": info["light"],

            "shadow": info["shadow"]
        }
    }


# ======================================================
# КАНАЛ ДЕНЕГ
# ======================================================

def interpret_money_channel(matrix):

    channel = matrix["money_channel"]

    interpretations = []

    for arcana in channel:

        info = get_arcana_info(arcana)

        interpretations.append({

            "arcana": arcana,

            "name": info["name"],

            "money": info["money"]
        })

    return {

        "position": "money_channel",

        "channel": interpretations,

        "summary":
            "Финансовый поток человека "
            "раскрывается через эти энергии."
    }


# ======================================================
# КАНАЛ ЛЮБВИ
# ======================================================

def interpret_love_channel(matrix):

    channel = matrix["love_channel"]

    interpretations = []

    for arcana in channel:

        info = get_arcana_info(arcana)

        interpretations.append({

            "arcana": arcana,

            "name": info["name"],

            "love": info["love"]
        })

    return {

        "position": "love_channel",

        "channel": interpretations,

        "summary":
            "Энергии отношений "
            "и эмоциональной реализации."
    }


# ======================================================
# ПРЕДНАЗНАЧЕНИЯ
# ======================================================

def interpret_destinations(matrix):

    destinations = matrix["destinations"]

    result = {}

    for key, arcana in destinations.items():

        info = get_arcana_info(arcana)

        result[key] = {

            "arcana": arcana,

            "name": info["name"],

            "mission": info["mission"]
        }

    return result


# ======================================================
# РОДОВЫЕ ЛИНИИ
# ======================================================

def interpret_generation_lines(matrix):

    male = matrix["male_generation_line"]

    female = matrix["female_generation_line"]

    male_result = []
    female_result = []

    for arcana in male:

        info = get_arcana_info(arcana)

        male_result.append({

            "arcana": arcana,

            "name": info["name"]
        })

    for arcana in female:

        info = get_arcana_info(arcana)

        female_result.append({

            "arcana": arcana,

            "name": info["name"]
        })

    return {

        "male_generation_line": male_result,

        "female_generation_line": female_result
    }


# ======================================================
# КАРМИЧЕСКИЙ ХВОСТ
# ======================================================

def interpret_karma_tail(matrix):

    karma = matrix["karma_tail"]

    result = {}

    for key, arcana in karma.items():

        info = get_arcana_info(arcana)

        result[key] = {

            "arcana": arcana,

            "name": info["name"],

            "shadow": info["shadow"]
        }

    return result


# ======================================================
# ВОЗРАСТНЫЕ АРКАНЫ
# ======================================================

def interpret_age_arcana(matrix, age: int):

    age_arcana = matrix["age_arcana"]

    arcana = age_arcana.get(str(age))

    if not arcana:

        return None

    info = get_arcana_info(arcana)

    return {

        "age": age,

        "arcana": arcana,

        "name": info["name"],

        "short": info["short"],

        "mission": info["mission"]
    }


# ======================================================
# ПОЛНЫЙ РАЗБОР
# ======================================================

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

        "destinations":
            interpret_destinations(matrix),

        "generation_lines":
            interpret_generation_lines(matrix),

        "karma_tail":
            interpret_karma_tail(matrix)
    }