from app.services.matrix_elements_service import (
    calculate_full_matrix
)


def calculate_matrix(
        birth_date: str
):
    """
    Главная функция расчёта матрицы.

    Используется:
    - при регистрации
    - при обновлении данных пользователя
    - для AI интерпретаций
    - для совместимости
    """

    matrix_data = calculate_full_matrix(
        birth_date
    )

    return matrix_data