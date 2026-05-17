from app.services.matrix_service import calculate_matrix


# =====================================
# КООРДИНАТЫ
# =====================================

POINT_COORDINATES = {

    # =================================
    # ОСНОВА
    # =================================

    "center": {"x": 0, "y": 0},

    "top": {"x": 0, "y": -300},
    "bottom": {"x": 0, "y": 300},

    "left": {"x": -300, "y": 0},
    "right": {"x": 300, "y": 0},

    # =================================
    # УГЛЫ
    # =================================

    "top_left": {"x": -220, "y": -220},
    "top_right": {"x": 220, "y": -220},

    "bottom_left": {"x": -220, "y": 220},
    "bottom_right": {"x": 220, "y": 220},

    # =================================
    # ВНУТРЕННИЕ ТОЧКИ
    # =================================

    "top_inner": {"x": 0, "y": -170},
    "bottom_inner": {"x": 0, "y": 170},

    "left_inner": {"x": -170, "y": 0},
    "right_inner": {"x": 170, "y": 0},

    # =================================
    # ДЕНЕЖНЫЙ КАНАЛ
    # =================================

    "money_1": {"x": 80, "y": 40},
    "money_2": {"x": 140, "y": 80},
    "money_3": {"x": 200, "y": 120},

    # =================================
    # ЛЮБОВНЫЙ КАНАЛ
    # =================================

    "love_1": {"x": 40, "y": 90},
    "love_2": {"x": 80, "y": 150},
    "love_3": {"x": 120, "y": 210},

    # =================================
    # МУЖСКОЙ РОД
    # =================================

    "male_1": {"x": -90, "y": -90},
    "male_2": {"x": -150, "y": -150},
    "male_3": {"x": -210, "y": -210},

    # =================================
    # ЖЕНСКИЙ РОД
    # =================================

    "female_1": {"x": 90, "y": -90},
    "female_2": {"x": 150, "y": -150},
    "female_3": {"x": 210, "y": -210},

    # =================================
    # КАРМИЧЕСКИЙ ХВОСТ
    # =================================

    "karmic_1": {"x": -60, "y": 120},
    "karmic_2": {"x": 0, "y": 180},
    "karmic_3": {"x": 60, "y": 240},
}


# =====================================
# ЛИНИИ
# =====================================

LINES = [

    # КВАДРАТ
    ("top", "right"),
    ("right", "bottom"),
    ("bottom", "left"),
    ("left", "top"),

    # ДИАГОНАЛИ
    ("top_left", "bottom_right"),
    ("top_right", "bottom_left"),

    # КРЕСТ
    ("top", "bottom"),
    ("left", "right"),

    # ВНУТРЕННИЙ КРЕСТ
    ("top_inner", "bottom_inner"),
    ("left_inner", "right_inner"),

    # МУЖСКОЙ РОД
    ("center", "male_1"),
    ("male_1", "male_2"),
    ("male_2", "male_3"),

    # ЖЕНСКИЙ РОД
    ("center", "female_1"),
    ("female_1", "female_2"),
    ("female_2", "female_3"),

    # ДЕНЬГИ
    ("center", "money_1"),
    ("money_1", "money_2"),
    ("money_2", "money_3"),

    # ЛЮБОВЬ
    ("center", "love_1"),
    ("love_1", "love_2"),
    ("love_2", "love_3"),

    # КАРМИЧЕСКИЙ ХВОСТ
    ("center", "karmic_1"),
    ("karmic_1", "karmic_2"),
    ("karmic_2", "karmic_3"),
]


# =====================================
# AGE CIRCLE
# =====================================

AGE_CIRCLE_COORDINATES = [

    {"age": 5, "x": -320, "y": -160},
    {"age": 15, "x": -140, "y": -320},
    {"age": 25, "x": 140, "y": -320},

    {"age": 35, "x": 320, "y": -160},
    {"age": 45, "x": 320, "y": 160},

    {"age": 55, "x": 140, "y": 320},
    {"age": 65, "x": -140, "y": 320},

    {"age": 75, "x": -320, "y": 160},
]


# =====================================
# СОЗДАНИЕ ТОЧКИ
# =====================================

def create_point(
        name,
        arcana
):

    return {

        "name": name,

        "arcana": arcana,

        "x": POINT_COORDINATES[name]["x"],

        "y": POINT_COORDINATES[name]["y"]
    }


# =====================================
# AGE CIRCLE
# =====================================

def build_age_circle(matrix):

    age_circle = []

    for point in AGE_CIRCLE_COORDINATES:

        age = point["age"]

        age_arcana = None

        for item in matrix["age_circle"]:

            if item["age"] == age:

                age_arcana = item["arcana"]

                break

        age_circle.append({

            "age": age,

            "arcana": age_arcana,

            "x": point["x"],

            "y": point["y"]
        })

    return age_circle


# =====================================
# CONNECTIONS
# =====================================

def build_connections():

    return [

        {
            "from": "center",
            "to": "money_1",
            "type": "money_channel"
        },

        {
            "from": "center",
            "to": "love_1",
            "type": "love_channel"
        },

        {
            "from": "center",
            "to": "male_1",
            "type": "male_generation"
        },

        {
            "from": "center",
            "to": "female_1",
            "type": "female_generation"
        },

        {
            "from": "center",
            "to": "karmic_1",
            "type": "karmic_tail"
        }
    ]


# =====================================
# ГЕОМЕТРИЯ МАТРИЦЫ
# =====================================

def build_matrix_geometry(
        birth_day,
        birth_month,
        birth_year
):

    matrix = calculate_matrix(
        birth_day,
        birth_month,
        birth_year
    )

    points = [

        # =================================
        # ОСНОВА
        # =================================

        create_point(
            "center",
            matrix["center"]
        ),

        create_point(
            "top",
            matrix["square"]["top"]
        ),

        create_point(
            "bottom",
            matrix["square"]["bottom"]
        ),

        create_point(
            "left",
            matrix["square"]["left"]
        ),

        create_point(
            "right",
            matrix["square"]["right"]
        ),

        # =================================
        # УГЛЫ
        # =================================

        create_point(
            "top_left",
            matrix["top_left"]
        ),

        create_point(
            "top_right",
            matrix["top_right"]
        ),

        create_point(
            "bottom_left",
            matrix["bottom_left"]
        ),

        create_point(
            "bottom_right",
            matrix["bottom_right"]
        ),

        # =================================
        # ВНУТРЕННИЕ ТОЧКИ
        # =================================

        create_point(
            "top_inner",
            matrix["top_inner"]
        ),

        create_point(
            "bottom_inner",
            matrix["bottom_inner"]
        ),

        create_point(
            "left_inner",
            matrix["left_inner"]
        ),

        create_point(
            "right_inner",
            matrix["right_inner"]
        ),

        # =================================
        # ДЕНЬГИ
        # =================================

        create_point(
            "money_1",
            matrix["money_channel"][0]
        ),

        create_point(
            "money_2",
            matrix["money_channel"][1]
        ),

        create_point(
            "money_3",
            matrix["money_channel"][2]
        ),

        # =================================
        # ЛЮБОВЬ
        # =================================

        create_point(
            "love_1",
            matrix["love_channel"][0]
        ),

        create_point(
            "love_2",
            matrix["love_channel"][1]
        ),

        create_point(
            "love_3",
            matrix["love_channel"][2]
        ),

        # =================================
        # МУЖСКОЙ РОД
        # =================================

        create_point(
            "male_1",
            matrix["male_generation_line"][0]
        ),

        create_point(
            "male_2",
            matrix["male_generation_line"][1]
        ),

        create_point(
            "male_3",
            matrix["male_generation_line"][2]
        ),

        # =================================
        # ЖЕНСКИЙ РОД
        # =================================

        create_point(
            "female_1",
            matrix["female_generation_line"][0]
        ),

        create_point(
            "female_2",
            matrix["female_generation_line"][1]
        ),

        create_point(
            "female_3",
            matrix["female_generation_line"][2]
        ),

        # =================================
        # КАРМИЧЕСКИЙ ХВОСТ
        # =================================

        create_point(
            "karmic_1",
            matrix["karmic_tail"][0]
        ),

        create_point(
            "karmic_2",
            matrix["karmic_tail"][1]
        ),

        create_point(
            "karmic_3",
            matrix["karmic_tail"][2]
        ),
    ]

    return {

        "points": points,

        "lines": LINES,

        "connections": build_connections(),

        "age_circle": build_age_circle(matrix),

        "matrix_data": matrix
    }