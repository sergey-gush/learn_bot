import logging
import settings
from datetime import date
import ephem
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext

logging.basicConfig(
    filename='bot.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

consts = {
    'Aries': 'Овен', 
    'Taurus': 'Телец',
    'Gemini': 'Близнецы',
    'Cancer': 'Рак',
    'Leo': 'Лев',
    'Virgo': 'Дева',
    'Libra': 'Весы',
    'Scorpius': 'Скорпион',
    'Sagittarius': 'Стрелец',
    'Capricornus': 'Козерог',
    'Aquarius': 'Водолей',
    'Pisces': 'Рыбы'
}

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('/start')
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def planets(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    text = update.message.text.split()
    planet_name = text[1]
    today = date.today()
    
    if planet_name == 'Марс':
        planet = ephem.Mars(today)
        planet_const = ephem.constellation(planet)
        await update.message.reply_text(f'{planet_name} в созвездии {consts[planet_const[1]]}')
    elif planet_name == 'Венера':
        planet = ephem.Venus(today)
        planet_const = ephem.constellation(planet)
        await update.message.reply_text(f'{planet_name} в созвездии {consts[planet_const[1]]}')
    elif planet_name == 'Меркурий':
        planet = ephem.Mercury(today)
        planet_const = ephem.constellation(planet)
        await update.message.reply_text(f'{planet_name} в созвездии {consts[planet_const[1]]}')
    elif planet_name == 'Луна':
        planet = ephem.Moon(today)
        planet_const = ephem.constellation(planet)
        await update.message.reply_text(f'{planet_name} в созвездии {consts[planet_const[1]]}')
    elif planet_name == 'Солнце':
        planet = ephem.Sun(today)
        planet_const = ephem.constellation(planet)
        await update.message.reply_text(f'{planet_name} в созвездии {consts[planet_const[1]]}')
    elif planet_name == 'Плутон':
        planet = ephem.Pluto(today)
        planet_const = ephem.constellation(planet)
        await update.message.reply_text(f'{planet_name} в созвездии {consts[planet_const[1]]}')
    elif planet_name == 'Юпитер':
        planet = ephem.Jupiter(today)
        planet_const = ephem.constellation(planet)
        await update.message.reply_text(f'{planet_name} в созвездии {consts[planet_const[1]]}')
    elif planet_name == 'Сатурн':
        planet = ephem.Saturn(today)
        planet_const = ephem.constellation(planet)
        await update.message.reply_text(f'{planet_name} в созвездии {consts[planet_const[1]]}')
    elif planet_name == 'Уран':
        planet = ephem.Uranus(today)
        planet_const = ephem.constellation(planet)
        await update.message.reply_text(f'{planet_name} в созвездии {consts[planet_const[1]]}')
    elif planet_name == 'Нептун':
        planet = ephem.Neptune(today)
        planet_const = ephem.constellation(planet)
        await update.message.reply_text(f'{planet_name} в созвездии {consts[planet_const[1]]}')


async def talk_to_me(update: Update, context: CallbackContext):
    text = update.message.text
    print(text)
    await update.message.reply_text(text)

def main():
    mybot = ApplicationBuilder().token(settings.API_KEY).build()

    start_handler = CommandHandler('start', hello)
    planet_handler = CommandHandler('planet', planets)
    msg_handler = MessageHandler(filters.TEXT, talk_to_me)
    mybot.add_handler(start_handler)
    mybot.add_handler(planet_handler)
    mybot.add_handler(msg_handler)

    logging.info('Started')
    mybot.run_polling()

if __name__ == '__main__':
    main()
