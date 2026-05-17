from app.services.matrix_geometry_service import (
    build_matrix_geometry
)


def reduce_to_22(number):

    while number > 22:

        number = sum(
            int(digit)
            for digit in str(number)
        )

    if number == 0:
        number = 22

    return number


def calculate_matrix(
        day,
        month,
        year
):

    year_sum = sum(
        int(digit)
        for digit in str(year)
    )

    day_arcana = reduce_to_22(day)

    month_arcana = reduce_to_22(month)

    year_arcana = reduce_to_22(year_sum)

    center = reduce_to_22(
        day_arcana +
        month_arcana +
        year_arcana
    )

    karmic_tail = [

        reduce_to_22(center + day_arcana),

        reduce_to_22(center + month_arcana),

        reduce_to_22(center + year_arcana)
    ]

    money_channel = [

        reduce_to_22(day_arcana + center),

        reduce_to_22(month_arcana + center)
    ]

    love_channel = [

        reduce_to_22(year_arcana + center),

        reduce_to_22(day_arcana + month_arcana)
    ]

    male_generation_line = [

        reduce_to_22(day_arcana + year_arcana),

        reduce_to_22(center + 5)
    ]

    female_generation_line = [

        reduce_to_22(month_arcana + year_arcana),

        reduce_to_22(center + 10)
    ]

    spiritual_destiny = reduce_to_22(
        center + 7
    )

    social_destiny = reduce_to_22(
        center + 14
    )

    material_destiny = reduce_to_22(
        center + 21
    )

    business_card = reduce_to_22(
        day_arcana +
        month_arcana
    )

    top_inner = reduce_to_22(
        day_arcana + center
    )

    bottom_inner = reduce_to_22(
        month_arcana + center
    )

    left_inner = reduce_to_22(
        year_arcana + center
    )

    right_inner = reduce_to_22(
        spiritual_destiny + center
    )

    year_energies = {}

    for age in range(1, 81):

        year_energies[age] = reduce_to_22(
            center + age
        )

    return {

        "day_arcana": day_arcana,

        "month_arcana": month_arcana,

        "year_arcana": year_arcana,

        "center": center,

        "business_card": business_card,

        "spiritual_destiny": spiritual_destiny,

        "social_destiny": social_destiny,

        "material_destiny": material_destiny,

        "karmic_tail": karmic_tail,

        "money_channel": money_channel,

        "love_channel": love_channel,

        "male_generation_line":
            male_generation_line,

        "female_generation_line":
            female_generation_line,

        "top_inner": top_inner,

        "bottom_inner": bottom_inner,

        "left_inner": left_inner,

        "right_inner": right_inner,

        "year_energies": year_energies
    }