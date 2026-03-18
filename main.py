import telebot
import os

# Отримуємо токен, який ми скоро додамо в налаштування
TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
 bot.reply_to(message, "Привіт! Бот Meest запущений через GitHub.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Ви написали: {message.text}")

if __name__ == "__main__":
    bot.infinity_polling()
