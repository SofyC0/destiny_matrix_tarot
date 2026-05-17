# app/services/matrix_elements_service.py

# ============================================================
# MATRIX OF DESTINY — NATALIA LADINI METHOD
# Полная логика расчёта матрицы судьбы 22 арканов
# ============================================================


# ============================================================
# ОСНОВНАЯ УТИЛИТА
# ============================================================

def reduce_to_22(number: int) -> int:

    """
    Сведение числа к диапазону 1-22
    """

    while number > 22:

        number = sum(
            int(digit)
            for digit in str(number)
        )

    if number == 0:
        number = 22

    return number


# ============================================================
# БАЗОВЫЕ АРКАНЫ
# ============================================================

def calculate_day_arcana(day: int):

    return reduce_to_22(day)


def calculate_month_arcana(month: int):

    return reduce_to_22(month)


def calculate_year_arcana(year: int):

    year_sum = sum(
        int(digit)
        for digit in str(year)
    )

    return reduce_to_22(year_sum)


# ============================================================
# ОСНОВА МАТРИЦЫ
# ============================================================

def calculate_bottom_arcana(
        day_arcana,
        month_arcana,
        year_arcana
):

    return reduce_to_22(
        day_arcana +
        month_arcana +
        year_arcana
    )


def calculate_center_arcana(
        top,
        left,
        right,
        bottom
):

    return reduce_to_22(
        top +
        left +
        right +
        bottom
    )


# ============================================================
# ВНУТРЕННИЙ КВАДРАТ
# ============================================================

def calculate_inner_square(
        top,
        left,
        right,
        bottom,
        center
):

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


# ============================================================
# ВНЕШНИЙ КВАДРАТ
# ============================================================

def calculate_outer_square(
        top,
        left,
        right,
        bottom
):

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


# ============================================================
# ДИАГОНАЛИ
# ============================================================

def calculate_diagonals(
        top,
        left,
        right,
        bottom,
        center
):

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


# ============================================================
# КАНАЛ ДЕНЕГ
# ============================================================

def calculate_money_channel(
        center,
        right,
        bottom
):

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


# ============================================================
# КАНАЛ ЛЮБВИ
# ============================================================

def calculate_love_channel(
        center,
        left,
        bottom
):

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


# ============================================================
# ВИЗИТКА
# ============================================================

def calculate_business_card(
        day_arcana,
        month_arcana
):

    """
    Визитка личности
    """

    return reduce_to_22(
        day_arcana +
        month_arcana
    )


# ============================================================
# КАРМИЧЕСКИЙ ХВОСТ
# ============================================================

def calculate_karma_tail(
        top,
        left,
        right
):

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


# ============================================================
# РОДОВЫЕ ЛИНИИ
# ============================================================

def calculate_male_generation_line(
        top,
        right
):

    return [

        reduce_to_22(
            top + right
        ),

        reduce_to_22(
            right * 2
        )
    ]


def calculate_female_generation_line(
        left,
        bottom
):

    return [

        reduce_to_22(
            left + bottom
        ),

        reduce_to_22(
            left * 2
        )
    ]


# ============================================================
# ПРЕДНАЗНАЧЕНИЯ
# ============================================================

def calculate_spiritual_destination(
        top,
        center
):

    """
    Духовное предназначение
    """

    return reduce_to_22(
        top + center
    )


def calculate_social_destination(
        left,
        center
):

    """
    Социальное предназначение
    """

    return reduce_to_22(
        left + center
    )


def calculate_material_destination(
        right,
        center
):

    """
    Материальное предназначение
    """

    return reduce_to_22(
        right + center
    )


def calculate_main_destination(
        spiritual,
        social,
        material
):

    """
    Главное предназначение души
    """

    return reduce_to_22(
        spiritual +
        social +
        material
    )


# ============================================================
# ВОЗРАСТНЫЕ АРКАНЫ
# ============================================================

def calculate_age_arcana_cycle(matrix_points):

    """
    Внешний круг жизни

    Энергии идут по кругу:
    верх -> право -> низ -> лево
    """

    cycle_points = [

        matrix_points["top"],
        matrix_points["top_right"],
        matrix_points["right"],
        matrix_points["bottom_right"],
        matrix_points["bottom"],
        matrix_points["bottom_left"],
        matrix_points["left"],
        matrix_points["top_left"]
    ]

    result = {}

    current_age = 0
    current_index = 0

    while current_age <= 80:

        energy = cycle_points[current_index]

        result[str(current_age)] = energy

        current_age += 1

        current_index += 1

        if current_index >= len(cycle_points):

            current_index = 0

    return result


# ============================================================
# ВСЯ МАТРИЦА
# ============================================================

def calculate_full_matrix(
        birth_day: int,
        birth_month: int,
        birth_year: int
):

    # ========================================================
    # БАЗОВЫЕ ЭНЕРГИИ
    # ========================================================

    top = calculate_day_arcana(
        birth_day
    )

    left = calculate_month_arcana(
        birth_month
    )

    right = calculate_year_arcana(
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

    # ========================================================
    # ВНУТРЕННИЙ КВАДРАТ
    # ========================================================

    inner_square = calculate_inner_square(
        top,
        left,
        right,
        bottom,
        center
    )

    # ========================================================
    # ВНЕШНИЙ КВАДРАТ
    # ========================================================

    outer_square = calculate_outer_square(
        top,
        left,
        right,
        bottom
    )

    # ========================================================
    # ДИАГОНАЛИ
    # ========================================================

    diagonals = calculate_diagonals(
        top,
        left,
        right,
        bottom,
        center
    )

    # ========================================================
    # КАНАЛЫ
    # ========================================================

    money_channel = calculate_money_channel(
        center,
        right,
        bottom
    )

    love_channel = calculate_love_channel(
        center,
        left,
        bottom
    )

    # ========================================================
    # ВИЗИТКА
    # ========================================================

    business_card = calculate_business_card(
        top,
        left
    )

    # ========================================================
    # РОД
    # ========================================================

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

    # ========================================================
    # КАРМА
    # ========================================================

    karma_tail = calculate_karma_tail(
        top,
        left,
        right
    )

    # ========================================================
    # ПРЕДНАЗНАЧЕНИЯ
    # ========================================================

    spiritual_destination = (
        calculate_spiritual_destination(
            top,
            center
        )
    )

    social_destination = (
        calculate_social_destination(
            left,
            center
        )
    )

    material_destination = (
        calculate_material_destination(
            right,
            center
        )
    )

    main_destination = (
        calculate_main_destination(
            spiritual_destination,
            social_destination,
            material_destination
        )
    )

    # ========================================================
    # ВОЗРАСТНЫЕ АРКАНЫ
    # ========================================================

    age_arcana = calculate_age_arcana_cycle({

        "top": top,

        "right": right,

        "bottom": bottom,

        "left": left,

        "top_left": outer_square["top_left"],

        "top_right": outer_square["top_right"],

        "bottom_left": outer_square["bottom_left"],

        "bottom_right": outer_square["bottom_right"]
    })

    # ========================================================
    # DEBUG
    # ========================================================

    print("================================")
    print("MATRIX CALCULATED")
    print("TOP =", top)
    print("LEFT =", left)
    print("RIGHT =", right)
    print("BOTTOM =", bottom)
    print("CENTER =", center)
    print("================================")

    # ========================================================
    # ГОТОВАЯ МАТРИЦА
    # ========================================================

    return {

        # ====================================================
        # ДАТА
        # ====================================================

        "birth_data": {

            "day": birth_day,

            "month": birth_month,

            "year": birth_year
        },

        # ====================================================
        # ОСНОВА
        # ====================================================

        "main_arcana": {

            "top": top,

            "left": left,

            "right": right,

            "bottom": bottom,

            "center": center
        },

        # ====================================================
        # КВАДРАТЫ
        # ====================================================

        "inner_square": inner_square,

        "outer_square": outer_square,

        # ====================================================
        # ДИАГОНАЛИ
        # ====================================================

        "diagonals": diagonals,

        # ====================================================
        # КАНАЛЫ
        # ====================================================

        "money_channel": money_channel,

        "love_channel": love_channel,

        # ====================================================
        # ВИЗИТКА
        # ====================================================

        "business_card": business_card,

        # ====================================================
        # КАРМА
        # ====================================================

        "karma_tail": karma_tail,

        # ====================================================
        # РОД
        # ====================================================

        "male_generation_line": (
            male_generation_line
        ),

        "female_generation_line": (
            female_generation_line
        ),

        # ====================================================
        # ПРЕДНАЗНАЧЕНИЯ
        # ====================================================

        "destinations": {

            "spiritual": (
                spiritual_destination
            ),

            "social": (
                social_destination
            ),

            "material": (
                material_destination
            ),

            "main": (
                main_destination
            )
        },

        # ====================================================
        # ВОЗРАСТНЫЕ АРКАНЫ
        # ====================================================

        "age_arcana": age_arcana
    }