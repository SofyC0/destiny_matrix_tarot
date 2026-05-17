from app.services.matrix_geometry_service import (
    MATRIX_GEOMETRY,
    MATRIX_LINES
)


# ==========================================
# SAFE GETTERS
# ==========================================

def get_list_value(data, index):

    if not isinstance(data, list):
        return None

    if index >= len(data):
        return None

    return data[index]


def get_dict_value(data, key):

    if not isinstance(data, dict):
        return None

    return data.get(key)


# ==========================================
# MATRIX VISUAL BUILDER
# ==========================================

def build_matrix_visual(matrix_data):
    """
    Строит визуальную структуру матрицы
    для frontend отображения
    """

    # ==========================================
    # КАНАЛЫ
    # ==========================================

    money_channel = matrix_data.get(
        "money_channel",
        []
    )

    love_channel = matrix_data.get(
        "love_channel",
        []
    )

    karmic_tail = matrix_data.get(
        "karma_tail",
        {}
    )

    # ==========================================
    # МАППИНГ ТОЧЕК
    # ==========================================

    mapping = {

        # основные точки
        "center": matrix_data.get("center"),

        "top": matrix_data.get("top"),

        "bottom": matrix_data.get("bottom"),

        "left": matrix_data.get("left"),

        "right": matrix_data.get("right"),

        "top_left": matrix_data.get("top_left"),

        "top_right": matrix_data.get("top_right"),

        "bottom_left": matrix_data.get("bottom_left"),

        "bottom_right": matrix_data.get("bottom_right"),

        # денежный канал
        "money_1": get_list_value(
            money_channel,
            0
        ),

        "money_2": get_list_value(
            money_channel,
            1
        ),

        # любовный канал
        "love_1": get_list_value(
            love_channel,
            0
        ),

        "love_2": get_list_value(
            love_channel,
            1
        ),

        # родовые линии
        "male_generation": matrix_data.get(
            "male_generation_line"
        ),

        "female_generation": matrix_data.get(
            "female_generation_line"
        ),

        # кармический хвост
        "karmic_1": get_dict_value(
            karmic_tail,
            "karmic_1"
        ),

        "karmic_2": get_dict_value(
            karmic_tail,
            "karmic_2"
        ),

        "karmic_3": get_dict_value(
            karmic_tail,
            "karmic_3"
        ),
    }

    # ==========================================
    # ТОЧКИ
    # ==========================================

    points = []

    for point_name, coords in MATRIX_GEOMETRY.items():

        points.append({

            "name": point_name,

            "arcana": mapping.get(point_name),

            "x": coords.get("x"),

            "y": coords.get("y")
        })

    # ==========================================
    # ЛИНИИ
    # ==========================================

    lines = []

    for line in MATRIX_LINES:

        if len(line) != 2:
            continue

        lines.append({

            "from": line[0],

            "to": line[1]
        })

    # ==========================================
    # RESULT
    # ==========================================

    return {

        "points": points,

        "lines": lines
    }