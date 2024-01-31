import telebot
import webbrowser

bot = telebot.TeleBot('6760301486:AAH8I1Az87BLCzkIwco4GY2k6rlORQOqLe8')

@bot.message_handler(commands = ['site', 'website'])
def site(message):
    webbrowser.open('https://developers.google.com/machine-learning')

@bot.message_handler(commands = ['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler(commands = ['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> information', parse_mode = 'html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID : {message.from_user.id}')

bot.polling(none_stop = True)