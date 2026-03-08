import telebot
import random
bot = telebot.TeleBot("8442666299:AAFE9uElziF5eME7UsvqiAhfXbnFXygqoFY")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Приветствую тебя, я бот для получения информации о погоде в твоем городе. Напиши мне название города и я тебе расскажу о погоде в нем. /help  /facts  /password")
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,"Это бот для получения информации о погоде. Напиши мне название города и я тебе расскажу о погоде в нем.")
@bot.message_handler(commands=['facts'])
def facts(message):
    bot.send_message(message.chat.id,"Погода - это состояние атмосферы в определенном месте и в определенное время. Она может быть солнечной, дождливой, снежной, ветреной и т.д. Погода влияет на нашу жизнь и настроение, а также на многие сферы деятельности, такие как сельское хозяйство, транспорт, туризм и т.д.")
@bot.message_handler(commands=['password'])
def password(message):
    sym = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    def gen_password(length):
        password = ""
        for i in range(12):
            password += random.choice(sym)
        return password
    new_password = gen_password(12)
    bot.send_message(message.chat.id,f"you are password is {new_password}")
bot.polling()