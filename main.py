
import telebot

TOKEN = 'ТВОЙ_ТОКЕН_ОТ_BOTFATHER'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Бот успешно работает!")

bot.polling()
