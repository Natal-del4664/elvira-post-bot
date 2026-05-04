import os
import sys
from typing import Any

import requests
from dotenv import load_dotenv


TELEGRAM_API_URL = "https://api.telegram.org/bot{token}/sendMessage"


def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Не найдена переменная окружения {name}. Проверьте файл .env")
    return value


def send_telegram_message(text: str) -> dict[str, Any]:
    """Отправляет сообщение в Telegram через Bot API."""
    load_dotenv()

    token = get_required_env("TELEGRAM_BOT_TOKEN")
    chat_id = get_required_env("TELEGRAM_CHAT_ID")

    response = requests.post(
        TELEGRAM_API_URL.format(token=token),
        json={
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
        },
        timeout=30,
    )

    try:
        data = response.json()
    except ValueError as exc:
        raise RuntimeError(f"Telegram вернул не JSON: {response.text}") from exc

    if not response.ok or not data.get("ok"):
        raise RuntimeError(f"Ошибка Telegram API: {data}")

    return data


def main() -> None:
    text = " ".join(sys.argv[1:]).strip()
    if not text:
        text = "Привет! Бот elvira-post-bot успешно отправляет сообщения."

    result = send_telegram_message(text)
    message_id = result.get("result", {}).get("message_id")
    print(f"Сообщение отправлено. message_id={message_id}")


if __name__ == "__main__":
    main()
