import telebot
    
bot = telebot.TeleBot("8088071512:AAEqopdAWGoRwnANpUM5fVVZqGKH_WWhP1M")
    
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
    
    # Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
        count_heh = int(message.text.split()[1]) if len(message.text.split())>1 else 5
        bot.reply_to(message,"he"*count_heh)
@bot.message_handler(commands=["ping"])
def on_ping(message):
    bot.reply_to(message, "Still alive and kicking!")

    # Запуск бота
bot.polling()
