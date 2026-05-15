def reduce_to_22(num: int):

    """
    Сведение числа к диапазону 1-22
    """

    while num > 22:

        num = sum(
            int(digit)
            for digit in str(num)
        )

    if num == 0:
        num = 22

    return num


# =========================================================
# ОСНОВНЫЕ АРКАНЫ
# =========================================================

def calculate_top_arcana(day: int):

    """
    Верхняя точка матрицы
    """

    return reduce_to_22(day)


def calculate_left_arcana(month: int):

    """
    Левая точка матрицы
    """

    return reduce_to_22(month)


def calculate_right_arcana(year: int):

    """
    Правая точка матрицы
    """

    year_sum = sum(
        int(digit)
        for digit in str(year)
    )

    return reduce_to_22(year_sum)


def calculate_bottom_arcana(
        top: int,
        left: int,
        right: int
):

    """
    Нижняя точка матрицы
    """

    return reduce_to_22(
        top +
        left +
        right
    )


# =========================================================
# ЦЕНТР
# =========================================================

def calculate_center_arcana(
        top: int,
        left: int,
        right: int,
        bottom: int
):

    """
    Центр матрицы
    """

    return reduce_to_22(
        top +
        left +
        right +
        bottom
    )


# =========================================================
# ВНУТРЕННИЕ АРКАНЫ
# =========================================================

def calculate_inner_arcana(
        top: int,
        left: int,
        right: int,
        bottom: int,
        center: int
):

    """
    Внутренние энергии
    """

    return {

        "top_inner": reduce_to_22(
            top + center
        ),

        "left_inner": reduce_to_22(
            left + center
        ),

        "right_inner": reduce_to_22(
            right + center
        ),

        "bottom_inner": reduce_to_22(
            bottom + center
        )
    }


# =========================================================
# КАРМИЧЕСКИЙ ХВОСТ
# =========================================================

def calculate_karma_tail(
        top: int,
        left: int,
        right: int
):

    """
    Кармические задачи
    """

    return {

        "karma_1": reduce_to_22(
            top + left
        ),

        "karma_2": reduce_to_22(
            left + right
        ),

        "karma_3": reduce_to_22(
            top + right
        )
    }


# =========================================================
# ЛИНИЯ ДЕНЕГ
# =========================================================

def calculate_money_line(
        center: int,
        right: int,
        bottom: int
):

    """
    Денежная линия
    """

    first = reduce_to_22(
        center + right
    )

    second = reduce_to_22(
        first + bottom
    )

    return [

        center,
        first,
        second
    ]


# =========================================================
# ЛИНИЯ ЛЮБВИ
# =========================================================

def calculate_love_line(
        center: int,
        left: int,
        bottom: int
):

    """
    Линия любви
    """

    first = reduce_to_22(
        center + left
    )

    second = reduce_to_22(
        first + bottom
    )

    return [

        center,
        first,
        second
    ]


# =========================================================
# МУЖСКОЙ РОД
# =========================================================

def calculate_male_generation_line(
        top: int,
        right: int
):

    """
    Мужской род
    """

    return [

        reduce_to_22(
            top + right
        ),

        reduce_to_22(
            right * 2
        )
    ]


# =========================================================
# ЖЕНСКИЙ РОД
# =========================================================

def calculate_female_generation_line(
        left: int,
        bottom: int
):

    """
    Женский род
    """

    return [

        reduce_to_22(
            left + bottom
        ),

        reduce_to_22(
            left * 2
        )
    ]


# =========================================================
# ЛИЧНОСТЬ
# =========================================================

def calculate_personality_arcana(
        top: int,
        left: int
):

    """
    Личность
    """

    return reduce_to_22(
        top + left
    )


# =========================================================
# ДУША
# =========================================================

def calculate_soul_arcana(
        center: int,
        top: int
):

    """
    Душа
    """

    return reduce_to_22(
        center + top
    )


# =========================================================
# ВОЗРАСТНЫЕ АРКАНЫ
# =========================================================

def calculate_age_arcana(
        birth_year: int
):

    """
    Аркан каждого возраста
    """

    result = {}

    for age in range(1, 81):

        age_value = reduce_to_22(
            birth_year + age
        )

        result[str(age)] = age_value

    return result


# =========================================================
# ВНЕШНИЙ КВАДРАТ
# =========================================================

def calculate_outer_square(
        top: int,
        left: int,
        right: int,
        bottom: int
):

    """
    Внешние углы матрицы
    """

    return {

        "top_left": reduce_to_22(
            top + left
        ),

        "top_right": reduce_to_22(
            top + right
        ),

        "bottom_left": reduce_to_22(
            left + bottom
        ),

        "bottom_right": reduce_to_22(
            right + bottom
        )
    }


# =========================================================
# ДИАГОНАЛИ
# =========================================================

def calculate_diagonals(
        top: int,
        left: int,
        right: int,
        bottom: int,
        center: int
):

    """
    Диагонали матрицы
    """

    return {

        "male_diagonal": [

            top,

            center,

            bottom
        ],

        "female_diagonal": [

            left,

            center,

            right
        ]
    }


# =========================================================
# ПОЛНАЯ МАТРИЦА
# =========================================================

def calculate_full_matrix(
        birth_day: int,
        birth_month: int,
        birth_year: int
):

    # =====================================================
    # ОСНОВНЫЕ ТОЧКИ
    # =====================================================

    top = calculate_top_arcana(
        birth_day
    )

    left = calculate_left_arcana(
        birth_month
    )

    right = calculate_right_arcana(
        birth_year
    )

    bottom = calculate_bottom_arcana(
        top,
        left,
        right
    )

    center = calculate_center_arcana(
        top,
        left,
        right,
        bottom
    )

    # =====================================================
    # ВНУТРЕННИЕ АРКАНЫ
    # =====================================================

    inner_arcana = calculate_inner_arcana(
        top,
        left,
        right,
        bottom,
        center
    )

    # =====================================================
    # ЛИНИИ
    # =====================================================

    money_line = calculate_money_line(
        center,
        right,
        bottom
    )

    love_line = calculate_love_line(
        center,
        left,
        bottom
    )

    male_generation_line = (
        calculate_male_generation_line(
            top,
            right
        )
    )

    female_generation_line = (
        calculate_female_generation_line(
            left,
            bottom
        )
    )

    # =====================================================
    # КАРМА
    # =====================================================

    karma_tail = calculate_karma_tail(
        top,
        left,
        right
    )

    # =====================================================
    # ЛИЧНОСТЬ И ДУША
    # =====================================================

    personality_arcana = (
        calculate_personality_arcana(
            top,
            left
        )
    )

    soul_arcana = (
        calculate_soul_arcana(
            center,
            top
        )
    )

    # =====================================================
    # ВНЕШНИЙ КВАДРАТ
    # =====================================================

    outer_square = calculate_outer_square(
        top,
        left,
        right,
        bottom
    )

    # =====================================================
    # ДИАГОНАЛИ
    # =====================================================

    diagonals = calculate_diagonals(
        top,
        left,
        right,
        bottom,
        center
    )

    # =====================================================
    # ВОЗРАСТНЫЕ АРКАНЫ
    # =====================================================

    age_arcana = calculate_age_arcana(
        birth_year
    )

    # =====================================================
    # DEBUG
    # =====================================================

    print("===================================")
    print("MATRIX CALCULATED")
    print("TOP =", top)
    print("LEFT =", left)
    print("RIGHT =", right)
    print("BOTTOM =", bottom)
    print("CENTER =", center)
    print("===================================")

    # =====================================================
    # ГОТОВАЯ МАТРИЦА
    # =====================================================

    return {

        # =================================================
        # ДАТА
        # =================================================

        "birth_data": {

            "day": birth_day,

            "month": birth_month,

            "year": birth_year
        },

        # =================================================
        # ГЛАВНЫЕ АРКАНЫ
        # =================================================

        "main_arcana": {

            "top": top,

            "left": left,

            "right": right,

            "bottom": bottom,

            "center": center
        },

        # =================================================
        # ВНУТРЕННИЕ АРКАНЫ
        # =================================================

        "inner_arcana": inner_arcana,

        # =================================================
        # ВНЕШНИЙ КВАДРАТ
        # =================================================

        "outer_square": outer_square,

        # =================================================
        # ЛИНИИ
        # =================================================

        "money_line": money_line,

        "love_line": love_line,

        # =================================================
        # РОД
        # =================================================

        "male_generation_line": (
            male_generation_line
        ),

        "female_generation_line": (
            female_generation_line
        ),

        # =================================================
        # ДИАГОНАЛИ
        # =================================================

        "diagonals": diagonals,

        # =================================================
        # КАРМА
        # =================================================

        "karma_tail": karma_tail,

        # =================================================
        # ДОПОЛНИТЕЛЬНО
        # =================================================

        "personality_arcana": (
            personality_arcana
        ),

        "soul_arcana": (
            soul_arcana
        ),

        # =================================================
        # ВОЗРАСТНЫЕ ЦИКЛЫ
        # =================================================

        "age_arcana": age_arcana
    }