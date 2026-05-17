from openai import OpenAI
from dotenv import load_dotenv

import os

from app.services.tarot_prompts import (
    TAROT_SYSTEM_PROMPT
)

load_dotenv()

client = OpenAI(

    api_key=os.getenv("DEEPSEEK_API_KEY"),

    base_url="https://api.deepseek.com"
)


def generate_tarot_reading(

        spread_name,
        cards
):

    cards_text = "\n".join(cards)

    user_prompt = f"""
Тип расклада:

{spread_name}

Выпавшие карты:

{cards_text}

Сделай полноценную трактовку
сочетания этих карт.

Объясни:
- что происходит
- скрытые энергии
- чувства
- конфликт карт
- итог энергии расклада

Отвечай как профессиональный таролог.
"""

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

        temperature=1.0
    )

    return response.choices[0].message.content