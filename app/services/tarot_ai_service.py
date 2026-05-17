import os

from dotenv import load_dotenv
from openai import OpenAI

from app.services.tarot_prompts import TAROT_SYSTEM_PROMPT
from app.data.tarot_spreads import TAROT_SPREADS

load_dotenv()

# ==========================================
# DEEPSEEK CLIENT
# ==========================================

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    timeout=60.0
)


# ==========================================
# ФОРМИРОВАНИЕ КАРТ С ПОЗИЦИЯМИ
# ==========================================

def build_cards_text(
        spread_key,
        cards
):
    spread = TAROT_SPREADS.get(spread_key)

    if not spread:
        return "\n".join(cards)

    positions = spread.get("positions", [])

    result = []

    for position, card in zip(positions, cards):
        result.append(
            f"{position}: {card}"
        )

    return "\n".join(result)


# ==========================================
# AI ТРАКТОВКА ТАРО
# ==========================================

def generate_tarot_reading(
        spread_key,
        cards
):
    """
    Генерация AI трактовки расклада
    """

    spread = TAROT_SPREADS.get(spread_key)

    if not spread:
        raise ValueError(
            f"Неизвестный расклад: {spread_key}"
        )

    spread_name = spread["name"]

    cards_text = build_cards_text(
        spread_key,
        cards
    )

    user_prompt = f"""
Тип расклада:

{spread_name}

Выпавшие карты:

{cards_text}

Сделай трактовку сочетания этих карт.

Обязательно используй структуру:

1. Общая энергия расклада
2. Что происходит в ситуации
3. Скрытые энергии
4. Чувства и эмоциональный фон
5. Конфликт или напряжение карт
6. Итог энергии расклада

Правила:
- не пиши огромный текст
- не используй психологические диагнозы
- не используй астрологию
- объясняй через символизм таро
- пиши как профессиональный таролог
- максимум 2-4 предложения на пункт
"""

    try:

        response = client.chat.completions.create(

            model="deepseek-chat",

            messages=[

                {
                    "role": "system",
                    "content": TAROT_SYSTEM_PROMPT
                },

                {
                    "role": "user",
                    "content": user_prompt
                }
            ],

            temperature=0.7,

            max_tokens=700
        )

        return response.choices[0].message.content

    except Exception as e:

        print(f"[TAROT AI ERROR] {e}")

        return (
            "Сейчас трактовка временно "
            "недоступна. Попробуйте позже."
        )