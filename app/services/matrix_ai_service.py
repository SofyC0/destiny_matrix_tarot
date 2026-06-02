# app/services/matrix_ai_service.py

import os

from dotenv import load_dotenv
from openai import OpenAI

from app.data.arcana_meanings import ARCANA

from app.services.premium_service import (
    can_ask_ai_question,
    can_access_full_ai
)

# =====================================================
# OPENROUTER / DEEPSEEK
# =====================================================

load_dotenv()

client = OpenAI(

    api_key=os.getenv("DEEPSEEK_API_KEY"),

    base_url="DEEPSEEK_UR"
)

# =====================================================
# AI MEMORY
# =====================================================

AI_MEMORY_LIMIT = 12

user_memory = {}

# =====================================================
# SYSTEM PROMPT
# =====================================================

SYSTEM_PROMPT = """
Ты — профессиональный AI интерпретатор Матрицы Судьбы.

ВАЖНО:

1. Анализируй ТОЛЬКО через матрицу судьбы.
2. Не используй астрологию.
3. Не используй психологические диагнозы.
4. Не используй эзотерический бред.
5. Не придумывай магию.
6. Не уходи в болезни и опасные темы.
7. Объясняй через энергии арканов.
8. Анализируй конфликты энергий.
9. Анализируй сильные и слабые стороны.
10. Отвечай как опытный интерпретатор.

Ты можешь анализировать:
- предназначение
- деньги
- отношения
- родовые линии
- кармический хвост
- внутренние конфликты
- сильные энергии
- внутренние точки
- каналы
- возрастные циклы

Пиши понятно и структурированно.
"""

# =====================================================
# MEMORY
# =====================================================

def save_to_memory(
        user_id,
        role,
        content
):

    if user_id not in user_memory:

        user_memory[user_id] = []

    user_memory[user_id].append({

        "role": role,

        "content": content
    })

    if len(user_memory[user_id]) > AI_MEMORY_LIMIT:

        user_memory[user_id] = user_memory[user_id][
            -AI_MEMORY_LIMIT:
        ]


def get_memory(user_id):

    return user_memory.get(user_id, [])


def clear_memory(user_id):

    user_memory[user_id] = []


# =====================================================
# ARCANA CONTEXT
# =====================================================

def build_arcana_context(matrix_data):

    used_arcanas = set()

    def extract(value):

        if isinstance(value, int):

            used_arcanas.add(value)

        elif isinstance(value, list):

            for item in value:

                extract(item)

        elif isinstance(value, dict):

            for item in value.values():

                extract(item)

    extract(matrix_data)

    context = ""

    for arcana in sorted(used_arcanas):

        if arcana in ARCANA:

            info = ARCANA[arcana]

            context += f"""

Аркан {arcana}
Название: {info.get("name", "")}

Свет:
{info.get("light", "")}

Тень:
{info.get("shadow", "")}

Предназначение:
{info.get("mission", "")}

Любовь:
{info.get("love", "")}

Деньги:
{info.get("money", "")}

==========================
"""

    return context


# =====================================================
# MATRIX SUMMARY
# =====================================================

def build_matrix_summary(matrix_data):

    return f"""
Центр: {matrix_data.get("center")}

Визитка:
{matrix_data.get("business_card")}

Духовное предназначение:
{matrix_data.get("spiritual_destiny")}

Социальное предназначение:
{matrix_data.get("social_destiny")}

Материальное предназначение:
{matrix_data.get("material_destiny")}

Денежный канал:
{matrix_data.get("money_channel")}

Любовный канал:
{matrix_data.get("love_channel")}

Кармический хвост:
{matrix_data.get("karmic_tail")}

Мужской род:
{matrix_data.get("male_generation_line")}

Женский род:
{matrix_data.get("female_generation_line")}
"""


# =====================================================
# AI REQUEST
# =====================================================

def ask_ai(messages):

    try:

        response = client.chat.completions.create(

            model="deepseek/deepseek-chat",

            messages=messages,

            temperature=0.7,

            max_tokens=1200
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"AI error: {str(e)}"


# =====================================================
# FULL MATRIX READING
# =====================================================

def generate_full_matrix_reading(
        matrix_data,
        is_premium=False
):

    if not can_access_full_ai(is_premium):

        return (
            "Полный AI анализ "
            "доступен только в Premium."
        )

    arcana_context = build_arcana_context(
        matrix_data
    )

    matrix_summary = build_matrix_summary(
        matrix_data
    )

    prompt = f"""
Матрица человека:

{matrix_summary}

Арканы:

{arcana_context}

Сделай:

1. Общий анализ личности
2. Главные энергии
3. Внутренние конфликты
4. Предназначение
5. Деньги
6. Отношения
7. Родовые программы
8. Кармические задачи
9. Сильные стороны
10. Слабые стороны

Отвечай структурированно.
"""

    messages = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },

        {
            "role": "user",
            "content": prompt
        }
    ]

    return ask_ai(messages)


# =====================================================
# ELEMENT READING
# =====================================================

def generate_element_reading(
        matrix_data,
        element_name,
        is_premium=False
):

    if not can_access_full_ai(is_premium):

        return (
            "AI разбор элементов "
            "доступен только в Premium."
        )

    element_value = matrix_data.get(
        element_name
    )

    if element_value is None:

        return "Элемент не найден."

    arcana_context = build_arcana_context(
        matrix_data
    )

    prompt = f"""
Матрица:

{matrix_data}

Арканы:

{arcana_context}

Сделай полный анализ элемента:

{element_name}

Значение:
{element_value}

Объясни:
- как проявляется
- сильные стороны
- слабые стороны
- проблемы
- потенциал
- как раскрывается
"""

    messages = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },

        {
            "role": "user",
            "content": prompt
        }
    ]

    return ask_ai(messages)


# =====================================================
# AI QUESTIONS
# =====================================================

def ask_matrix_question(
        user_id,
        matrix_data,
        question,
        is_premium=False,
        ai_questions_used=0
):

    if not can_ask_ai_question(
            is_premium,
            ai_questions_used
    ):

        return (
            "Лимит AI вопросов "
            "для FREE тарифа исчерпан."
        )

    arcana_context = build_arcana_context(
        matrix_data
    )

    memory = get_memory(user_id)

    prompt = f"""
Матрица:

{matrix_data}

Арканы:

{arcana_context}

Вопрос:

{question}

Отвечай только через матрицу.
"""

    messages = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(memory)

    messages.append({

        "role": "user",

        "content": prompt
    })

    answer = ask_ai(messages)

    save_to_memory(
        user_id,
        "user",
        question
    )

    save_to_memory(
        user_id,
        "assistant",
        answer
    )

    return answer