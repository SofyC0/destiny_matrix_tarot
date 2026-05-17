from app.services.matrix_geometry_service import (
    MATRIX_GEOMETRY,
    MATRIX_LINES
)


def build_matrix_visual(matrix_data):

    points = []

    # ==========================================
    # МАППИНГ ТОЧЕК
    # ==========================================

    mapping = {

        "center": matrix_data.get("center"),

        "top": matrix_data.get("top"),

        "bottom": matrix_data.get("bottom"),

        "left": matrix_data.get("left"),

        "right": matrix_data.get("right"),

        "top_left": matrix_data.get("top_left"),

        "top_right": matrix_data.get("top_right"),

        "bottom_left": matrix_data.get("bottom_left"),

        "bottom_right": matrix_data.get("bottom_right"),

        "money_1": matrix_data.get("money_channel", [None])[0],

        "money_2": matrix_data.get("money_channel", [None, None])[1],

        "love_1": matrix_data.get("love_channel", [None])[0],

        "love_2": matrix_data.get("love_channel", [None, None])[1],

        "male_generation": matrix_data.get("male_generation_line"),

        "female_generation": matrix_data.get("female_generation_line"),

        "karmic_1": matrix_data.get("karmic_tail", [None])[0],

        "karmic_2": matrix_data.get("karmic_tail", [None, None])[1],

        "karmic_3": matrix_data.get("karmic_tail", [None, None, None])[2],
    }

    # ==========================================
    # СОЗДАЕМ ТОЧКИ
    # ==========================================

    for point_name, coords in MATRIX_GEOMETRY.items():

        points.append({

            "name": point_name,

            "arcana": mapping.get(point_name),

            "x": coords["x"],

            "y": coords["y"]
        })

    # ==========================================
    # ЛИНИИ
    # ==========================================

    lines = []

    for line in MATRIX_LINES:

        lines.append({

            "from": line[0],

            "to": line[1]
        })

    return {

        "points": points,

        "lines": lines
    }