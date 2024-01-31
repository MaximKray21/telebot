import telebot
from telebot import types

bot = telebot.TeleBot('6760301486:AAH8I1Az87BLCzkIwco4GY2k6rlORQOqLe8')

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    b1 = types.KeyboardButton('WTF')
    markup.row(b1)
    file = open('./photoi.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup = markup)

    # bot.send_audio(message.chat.id, audiofile_name, reply_markup = markup)
    # bot.send_message(message.chat.id, 'Hello', reply_markup = markup)

    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'WTF':
        bot.send_message(message.chat.id, 'fuck u izikiel')

@bot.message_handler(content_types = ['audio', 'video', 'photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton('Go to web', url = 'https://vk.com/m_cry_s_man')
    markup.row(b1)
    b2 = types.InlineKeyboardButton('delete Photo', callback_data = 'delete')
    b3 = types.InlineKeyboardButton('edit text', callback_data = 'edit')
    markup.row(b2, b3)

    # markup.add(types.InlineKeyboardButton('edit text', callback_data = 'edit text'))

    bot.reply_to(message, 'Fuck u', reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edited text', callback.message.chat.id, callback.message.message_id)


bot.polling(none_stop = True)