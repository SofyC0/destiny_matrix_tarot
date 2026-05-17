user_memory = {}


def save_to_memory(
        user_id,
        question,
        answer
):

    if user_id not in user_memory:

        user_memory[user_id] = []

    user_memory[user_id].append({

        "question": question,

        "answer": answer
    })

    # лимит памяти
    user_memory[user_id] = user_memory[user_id][-10:]


def get_memory(user_id):

    return user_memory.get(user_id, [])