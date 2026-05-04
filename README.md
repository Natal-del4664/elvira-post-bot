# elvira-post-bot

Простой стартовый проект Telegram-бота для отправки сообщений в указанный чат.

## Что внутри

- `main.py` — отправляет сообщение в Telegram через Bot API.
- `requirements.txt` — зависимости Python.
- `.env.example` — пример файла с секретами.
- `.gitignore` — исключает `.env`, виртуальное окружение и служебные файлы.

## Как запустить локально

1. Скачайте репозиторий через **Code → Download ZIP** или клонируйте его.
2. Откройте папку проекта в PowerShell.
3. Создайте виртуальное окружение:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

4. Установите зависимости:

```powershell
pip install -r requirements.txt
```

5. Скопируйте `.env.example` в `.env`:

```powershell
copy .env.example .env
```

6. Откройте `.env` и вставьте свои значения:

```env
TELEGRAM_BOT_TOKEN=ваш_новый_токен
TELEGRAM_CHAT_ID=ваш_chat_id
```

7. Отправьте тестовое сообщение:

```powershell
python main.py "Привет из моего Telegram-бота!"
```

## Безопасность

Не добавляйте настоящий `.env` в GitHub. В `.gitignore` уже есть правило, которое защищает этот файл от случайной загрузки.
