import os
import requests

from dotenv import load_dotenv

from app.services.matrix_service import (
    calculate_matrix
)

load_dotenv()

DEEPSEEK_API_KEY = os.getenv(
    "DEEPSEEK_API_KEY"
)

DEEPSEEK_URL = os.getenv(
    "DEEPSEEK_URL"
)


def ask_deepseek(prompt):

    headers = {

        "Authorization":
            f"Bearer {DEEPSEEK_API_KEY}",

        "Content-Type":
            "application/json"
    }

    data = {

        "model": "deepseek-chat",

        "messages": [

            {
                "role": "user",

                "content": prompt
            }
        ]
    }

    response = requests.post(
        DEEPSEEK_URL,
        headers=headers,
        json=data
    )

    result = response.json()

    return result["choices"][0]["message"]["content"]


def generate_full_matrix_analysis(
        day,
        month,
        year
):

    matrix = calculate_matrix(
        day,
        month,
        year
    )

    prompt = f"""

    Сделай полный анализ матрицы судьбы.

    Матрица:
    {matrix}

    """

    return ask_deepseek(prompt)


def generate_element_analysis(
        element,
        day,
        month,
        year
):

    matrix = calculate_matrix(
        day,
        month,
        year
    )

    value = matrix.get(element)

    prompt = f"""

    Проанализируй элемент матрицы:

    {element}

    Значение:
    {value}

    """

    return ask_deepseek(prompt)