from app.data.arcana_meanings import ARCANA_MEANINGS


def interpret_arcana(arcana):

    return ARCANA_MEANINGS.get(
        arcana,
        "Нет описания"
    )


def interpret_matrix(matrix):

    result = {}

    for key, value in matrix.items():

        if isinstance(value, int):

            result[key] = interpret_arcana(value)

        elif isinstance(value, list):

            result[key] = [

                interpret_arcana(v)

                for v in value
            ]

    return result