# 🔮 Destiny Matrix Tarot

Проект представляет собой веб-приложение для расчета **Матрицы Судьбы** по дате рождения с использованием методики **22 Арканов**, а также получения AI-интерпретации результатов и работы с Таро.

## Возможности

- 🔐 Регистрация и авторизация пользователей
- 🧮 Расчет Матрицы Судьбы
- 🔮 Интерпретация арканов
- 🤖 AI-анализ матрицы
- 🃏 Таро-расклады и значения карт
- 👤 Хранение данных пользователей

## Стек технологий

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT
- Uvicorn

## Структура проекта

```
destiny_matrix_tarot/
├── backend/      # Backend приложения
├── taroGUI/      # Пользовательский интерфейс
├── tests/        # Тесты
├── run.py
└── requirements.txt
```

## Установка

Клонируйте репозиторий:

```bash
git clone https://github.com/SofyC0/destiny_matrix_tarot.git
cd destiny_matrix_tarot
```

Создайте виртуальное окружение и установите зависимости:

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

Установка зависимостей:

```bash
pip install -r requirements.txt
```

## Запуск

```bash
python run.py
```

После запуска приложение будет доступно по адресу:

```
http://127.0.0.1:8000
```

Документация API:

```
http://127.0.0.1:8000/docs
```

## Автор

**Софья Шатова**

GitHub: https://github.com/SofyC0
