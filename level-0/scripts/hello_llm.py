"""
Level 0 / optional: первый вызов LLM из Python.

Установка (пример для OpenAI):
  pip install openai

Ключ (не коммить!):
  export OPENAI_API_KEY="sk-..."

Запуск:
  python level-0/scripts/hello_llm.py
"""

from __future__ import annotations

import os
import sys


def main() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Нет OPENAI_API_KEY. Создай ключ у провайдера и экспортируй в окружение.")
        sys.exit(1)

    try:
        from openai import OpenAI
    except ImportError:
        print("Пакет openai не установлен. Сделай: pip install openai")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Ты спокойный преподаватель. Отвечай коротко и ясно.",
            },
            {
                "role": "user",
                "content": "Объясни, что такое LLM, простыми словами. В конце дай 5 терминов в JSON.",
            },
        ],
    )

    message = response.choices[0].message.content
    print("=== Ответ модели ===")
    print(message)

    usage = getattr(response, "usage", None)
    if usage is not None:
        print("\n=== Usage ===")
        print(f"prompt_tokens: {usage.prompt_tokens}")
        print(f"completion_tokens: {usage.completion_tokens}")
        print(f"total_tokens: {usage.total_tokens}")


if __name__ == "__main__":
    main()
