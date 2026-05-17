def build_matrix_context(matrix):

    return f"""

ЦЕНТР:
{matrix.get("center")}

ВИЗИТКА:
{matrix.get("business_card")}

ДУХОВНОЕ ПРЕДНАЗНАЧЕНИЕ:
{matrix.get("spiritual_destiny")}

СОЦИАЛЬНОЕ ПРЕДНАЗНАЧЕНИЕ:
{matrix.get("social_destiny")}

МАТЕРИАЛЬНОЕ ПРЕДНАЗНАЧЕНИЕ:
{matrix.get("material_destiny")}

КАРМИЧЕСКИЙ ХВОСТ:
{matrix.get("karmic_tail")}

ДЕНЕЖНЫЙ КАНАЛ:
{matrix.get("money_channel")}

ЛЮБОВНЫЙ КАНАЛ:
{matrix.get("love_channel")}

МУЖСКОЙ РОД:
{matrix.get("male_generation_line")}

ЖЕНСКИЙ РОД:
{matrix.get("female_generation_line")}

ВНУТРЕННИЕ ТОЧКИ:
{matrix.get("inner_points")}
"""