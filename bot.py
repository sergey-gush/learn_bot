import logging
import settings
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext

logging.basicConfig(
    filename='bot.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('/start')
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def talk_to_me(update: Update, context: CallbackContext):
    text = update.message.text
    print(text)
    await update.message.reply_text(text)


def main():
    mybot = ApplicationBuilder().token(settings.API_KEY).build()

    start_handler = CommandHandler('start', hello)
    msg_handler = MessageHandler(filters.TEXT, talk_to_me)
    mybot.add_handler(start_handler)
    mybot.add_handler(msg_handler)

    logging.info('Started')
    mybot.run_polling()

if __name__ == '__main__':
    main()
