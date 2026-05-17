from app.services.matrix_service import (
    calculate_matrix
)

POINT_COORDINATES = {

    "center": {"x": 0, "y": 0},

    "top": {"x": 0, "y": -300},

    "bottom": {"x": 0, "y": 300},

    "left": {"x": -300, "y": 0},

    "right": {"x": 300, "y": 0}
}


LINES = [

    ("top", "right"),

    ("right", "bottom"),

    ("bottom", "left"),

    ("left", "top")
]


def build_matrix_geometry(
        day,
        month,
        year
):

    matrix = calculate_matrix(
        day,
        month,
        year
    )

    points = [

        {
            "name": "center",

            "arcana": matrix["center"],

            **POINT_COORDINATES["center"]
        },

        {
            "name": "top",

            "arcana": matrix["day_arcana"],

            **POINT_COORDINATES["top"]
        },

        {
            "name": "bottom",

            "arcana": matrix["month_arcana"],

            **POINT_COORDINATES["bottom"]
        }
    ]

    return {

        "points": points,

        "lines": LINES,

        "matrix_data": matrix
    }