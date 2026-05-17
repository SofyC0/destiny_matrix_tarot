import os

from openai import OpenAI

from app.data.arcana_meanings import ARCANA_MEANINGS

from app.services.premium_service import (can_access_matrix_element, can_ask_ai_question)

# ==========================================
# DEEPSEEK CLIENT
# ==========================================

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


# ==========================================
# ПОДГОТОВКА АРКАНОВ
# ==========================================

def build_arcana_context(matrix_data):
    """
    Собирает описания арканов матрицы
    """

    used_arcanas = set()

    for value in matrix_data.values():

        if isinstance(value, int):
            used_arcanas.add(value)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, int):
                    used_arcanas.add(item)

    context = ""

    for arcana in used_arcanas:

        if arcana in ARCANA_MEANINGS:

            meaning = ARCANA_MEANINGS[arcana]

            context += f"""
Аркан {arcana}

Название:
{meaning.get("name")}

Свет:
{meaning.get("light")}

Тень:
{meaning.get("shadow")}

Предназначение:
{meaning.get("purpose")}

Отношения:
{meaning.get("relationships")}

Деньги:
{meaning.get("money")}

====================
"""

    return context


# ==========================================
# SYSTEM PROMPT
# ==========================================

SYSTEM_PROMPT = """
Ты — AI интерпретатор Матрицы Судьбы
по системе Наталии Ладини.

Твои правила:

1. Анализируй ТОЛЬКО матрицу.
2. Не используй астрологию.
3. Не используй психологические диагнозы.
4. Не придумывай магию.
5. Не говори про болезни.
6. Не давай опасных советов.
7. Объясняй через энергии арканов.
8. Отвечай мягко и понятно.
9. Не пиши огромные тексты.
10. Пиши как профессиональный интерпретатор матрицы.

Ты должен:
- анализировать конфликты энергий
- сильные стороны
- предназначение
- денежный канал
- отношения
- кармические задачи
- родовые линии

Но ТОЛЬКО через матрицу.
"""


# ==========================================
# AI АНАЛИЗ ВСЕЙ МАТРИЦЫ
# ==========================================

def generate_full_matrix_analysis(matrix_data):

    arcana_context = build_arcana_context(matrix_data)

    prompt = f"""
Вот матрица человека:

{matrix_data}

Вот значения арканов:

{arcana_context}

Сделай:
1. Общий анализ личности
2. Сильные энергии
3. Внутренние конфликты
4. Предназначение
5. Денежный канал
6. Отношения
7. Родовые задачи
8. Кармический хвост

Пиши структурированно.
"""

    response = client.chat.completions.create(
        model="deepseek/deepseek-chat",

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7,
        max_tokens=1200
    )

    return response.choices[0].message.content


# ==========================================
# AI АНАЛИЗ ЭЛЕМЕНТА
# ==========================================

def generate_element_analysis(
        matrix_data,
        element_name
):
    arcana_context = build_arcana_context(matrix_data)

    prompt = f"""
Матрица:

{matrix_data}

Арканы:

{arcana_context}

Сделай подробный анализ элемента:

{element_name}

Объясни:
- сильные стороны
- слабые стороны
- как проявляется
- как проработать
"""

    response = client.chat.completions.create(
        model="deepseek/deepseek-chat",

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7,
        max_tokens=700
    )

    return response.choices[0].message.content


# ==========================================
# AI ОТВЕТЫ НА ВОПРОСЫ
# ==========================================

def ask_matrix_question(
        matrix_data,
        question
):
    arcana_context = build_arcana_context(matrix_data)

    prompt = f"""
Матрица человека:

{matrix_data}

Арканы:

{arcana_context}

Вопрос пользователя:

{question}

Отвечай только через матрицу судьбы.
Не уходи в психологию.
Не используй астрологию.
"""

    response = client.chat.completions.create(
        model="deepseek/deepseek-chat",

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7,
        max_tokens=600
    )

    return response.choices[0].message.content