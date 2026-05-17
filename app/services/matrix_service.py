from datetime import datetime


# =========================
# ОСНОВНАЯ СВЕРТКА В 1-22
# =========================

def reduce_to_22(num: int) -> int:
    """
    Сворачивает число к диапазону 1-22
    """
    while num > 22:
        num = sum(int(digit) for digit in str(num))

    if num == 0:
        num = 22

    return num


# =========================
# БАЗОВЫЕ ЭНЕРГИИ
# =========================

def calculate_base_arcanas(day, month, year):
    year_sum = sum(int(d) for d in str(year))

    return {
        "day_arcana": reduce_to_22(day),
        "month_arcana": reduce_to_22(month),
        "year_arcana": reduce_to_22(year_sum),
    }


# =========================
# ЦЕНТР МАТРИЦЫ
# =========================

def calculate_center(day_arcana, month_arcana, year_arcana):
    return reduce_to_22(
        day_arcana + month_arcana + year_arcana
    )


# =========================
# ВИЗИТКА
# =========================

def calculate_business_card(day_arcana, month_arcana):
    return reduce_to_22(day_arcana + month_arcana)


# =========================
# ПРЕДНАЗНАЧЕНИЯ
# =========================

def calculate_destinies(
        day_arcana,
        month_arcana,
        year_arcana,
        center
):
    spiritual = reduce_to_22(day_arcana + center)

    social = reduce_to_22(month_arcana + center)

    material = reduce_to_22(year_arcana + center)

    return {
        "spiritual_destiny": spiritual,
        "social_destiny": social,
        "material_destiny": material,
    }


# =========================
# КАРМИЧЕСКИЙ ХВОСТ
# =========================

def calculate_karmic_tail(
        day_arcana,
        month_arcana,
        year_arcana
):
    karmic_1 = reduce_to_22(day_arcana + month_arcana)

    karmic_2 = reduce_to_22(month_arcana + year_arcana)

    karmic_3 = reduce_to_22(day_arcana + year_arcana)

    return {
        "karmic_tail": [
            karmic_1,
            karmic_2,
            karmic_3
        ]
    }


# =========================
# РОДОВЫЕ ЛИНИИ
# =========================

def calculate_ancestral_lines(
        day_arcana,
        month_arcana,
        year_arcana,
        center
):
    male_line = [
        reduce_to_22(day_arcana + center),
        reduce_to_22(day_arcana + year_arcana),
        reduce_to_22(center + year_arcana),
    ]

    female_line = [
        reduce_to_22(month_arcana + center),
        reduce_to_22(month_arcana + year_arcana),
        reduce_to_22(center + month_arcana),
    ]

    return {
        "male_generation_line": male_line,
        "female_generation_line": female_line,
    }


# =========================
# ДЕНЕЖНЫЙ КАНАЛ
# =========================

def calculate_money_channel(
        center,
        business_card,
        material_destiny
):
    money_line = [
        center,
        business_card,
        material_destiny
    ]

    strong = [
        x for x in money_line
        if x in [1,3,4,7,8,10,15,19,21]
    ]

    weak = [
        x for x in money_line
        if x in [12,13,16,18]
    ]

    return {
        "money_channel": money_line,
        "strong_money_energies": strong,
        "weak_money_energies": weak,
    }


# =========================
# ЛЮБОВНЫЙ КАНАЛ
# =========================

def calculate_love_channel(
        center,
        spiritual_destiny,
        social_destiny
):
    love_line = [
        center,
        spiritual_destiny,
        social_destiny
    ]

    harmonious = [
        x for x in love_line
        if x in [2,3,6,14,17,19]
    ]

    problematic = [
        x for x in love_line
        if x in [15,16,18]
    ]

    return {
        "love_channel": love_line,
        "harmonious_energies": harmonious,
        "problematic_energies": problematic,
    }


# =========================
# ВНУТРЕННИЕ ТОЧКИ
# =========================

def calculate_inner_points(
        day_arcana,
        month_arcana,
        year_arcana,
        center
):
    top_inner = reduce_to_22(day_arcana + center)

    bottom_inner = reduce_to_22(month_arcana + center)

    left_inner = reduce_to_22(day_arcana + month_arcana)

    right_inner = reduce_to_22(year_arcana + center)

    diagonal_1 = reduce_to_22(top_inner + bottom_inner)

    diagonal_2 = reduce_to_22(left_inner + right_inner)

    return {
        "top_inner": top_inner,
        "bottom_inner": bottom_inner,
        "left_inner": left_inner,
        "right_inner": right_inner,
        "diagonal_1": diagonal_1,
        "diagonal_2": diagonal_2,
    }


# =========================
# ВОЗРАСТНОЙ КРУГ
# =========================

def calculate_age_arcana(
        birth_day,
        birth_month,
        birth_year,
        age
):
    total = (
            birth_day
            + birth_month
            + sum(int(d) for d in str(birth_year))
            + age
    )

    return reduce_to_22(total)


# =========================
# ЦИКЛЫ ЖИЗНИ
# =========================

def calculate_life_cycles(
        birth_day,
        birth_month,
        birth_year
):
    cycles = {}

    for age in [5, 15, 25, 35, 45, 55, 65, 75]:
        cycles[f"{age}_years"] = calculate_age_arcana(
            birth_day,
            birth_month,
            birth_year,
            age
        )

    return cycles


# =========================
# ЭНЕРГИИ ПО ГОДАМ
# =========================

def calculate_year_energies(
        birth_day,
        birth_month,
        birth_year,
        years_ahead=15
):
    current_year = datetime.now().year

    result = []

    for i in range(years_ahead):
        year = current_year + i

        energy = reduce_to_22(
            birth_day
            + birth_month
            + sum(int(d) for d in str(year))
        )

        result.append({
            "year": year,
            "energy": energy
        })

    return result


# =========================
# ПОЛНАЯ МАТРИЦА
# =========================

def calculate_matrix(
        birth_day,
        birth_month,
        birth_year
):
    base = calculate_base_arcanas(
        birth_day,
        birth_month,
        birth_year
    )

    center = calculate_center(
        base["day_arcana"],
        base["month_arcana"],
        base["year_arcana"]
    )

    business_card = calculate_business_card(
        base["day_arcana"],
        base["month_arcana"]
    )

    destinies = calculate_destinies(
        base["day_arcana"],
        base["month_arcana"],
        base["year_arcana"],
        center
    )

    karmic = calculate_karmic_tail(
        base["day_arcana"],
        base["month_arcana"],
        base["year_arcana"]
    )

    ancestral = calculate_ancestral_lines(
        base["day_arcana"],
        base["month_arcana"],
        base["year_arcana"],
        center
    )

    money = calculate_money_channel(
        center,
        business_card,
        destinies["material_destiny"]
    )

    love = calculate_love_channel(
        center,
        destinies["spiritual_destiny"],
        destinies["social_destiny"]
    )

    inner_points = calculate_inner_points(
        base["day_arcana"],
        base["month_arcana"],
        base["year_arcana"],
        center
    )

    cycles = calculate_life_cycles(
        birth_day,
        birth_month,
        birth_year
    )

    yearly = calculate_year_energies(
        birth_day,
        birth_month,
        birth_year
    )

    return {
        **base,

        "center": center,

        "business_card": business_card,

        **destinies,

        **karmic,

        **ancestral,

        **money,

        **love,

        **inner_points,

        "life_cycles": cycles,

        "year_energies": yearly,
    }