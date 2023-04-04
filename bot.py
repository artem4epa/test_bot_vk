import os

import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')
VK_TOKEN = os.getenv('VK_ACCES_TOKEN')
ENDPOINT = os.getenv('ENDPOINT')

def request():
    headers = {'Authorization': f'Bearer {VK_TOKEN}'}
    request = requests.post(url=ENDPOINT, headers=headers)
    result = request.json()['response']['count']
    return result

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Привет, я бот, который знает сколько девушек, проживающих в Питере с именем на букву 'В' зарегистрированно в ВК. Если хотите узнать число наберите команду /question"
    )

async def question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"В соцсети ВК зарегистрированно {request()} девушек с именем на букву 'В', проживающих в Санкт Петербурге."
    )

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler('start', start)
    question_handler = CommandHandler('question', question)
    application.add_handlers([start_handler, question_handler])
    application.run_polling()
