from collections import defaultdict
from threading import Lock


# ==========================================
# IN-MEMORY STORAGE
# ==========================================

user_memory = defaultdict(list)

memory_lock = Lock()

MAX_MEMORY_PER_USER = 10

MAX_ANSWER_LENGTH = 3000


# ==========================================
# SAVE TO MEMORY
# ==========================================

def save_to_memory(
        user_id,
        question,
        answer
):
    """
    Сохраняет последние AI диалоги пользователя
    """

    if not user_id:
        return

    if not question:
        return

    if not answer:
        return

    question = str(question).strip()

    answer = str(answer).strip()

    if not question:
        return

    if not answer:
        return

    # ограничиваем размер ответа
    answer = answer[:MAX_ANSWER_LENGTH]

    with memory_lock:

        user_memory[user_id].append({

            "question": question,

            "answer": answer
        })

        # храним только последние N сообщений
        user_memory[user_id] = user_memory[user_id][
            -MAX_MEMORY_PER_USER:
        ]


# ==========================================
# GET MEMORY
# ==========================================

def get_memory(user_id):
    """
    Получить память пользователя
    """

    with memory_lock:

        return list(
            user_memory.get(user_id, [])
        )


# ==========================================
# CLEAR MEMORY
# ==========================================

def clear_memory(user_id):
    """
    Очистить память пользователя
    """

    with memory_lock:

        if user_id in user_memory:

            del user_memory[user_id]


# ==========================================
# MEMORY SIZE
# ==========================================

def get_memory_size(user_id):

    with memory_lock:

        return len(
            user_memory.get(user_id, [])
        )