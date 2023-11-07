import openai
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

# Ваш API ключ від OpenAI
openai.api_key = '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'

def respond_to_user(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_message,
        max_tokens=1000  # Максимальна довжина відповіді
    )
    reply = response.choices[0].text
    update.message.reply_text(reply)

def main() -> None:
    # Ваш токен Telegram-бота
    TELEGRAM_TOKEN = '6783827119:AAHbkkMnEzUBo5M2WDPhqlAhEVe04n_yZPU'

    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Видаліть обробник повідомлень
    # dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, respond_to_user))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
