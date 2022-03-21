import telebot
import datetime

bot = telebot.TeleBot('5218439106:AAEqXO-5wXGh5I9zsDNkEPbUPMDbHQLforA')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Я пробил информацию:\n'
                                      f'ID чата: {message.chat.id}\n'
                                      f'ID юзера {message.from_user.id}\n'
                                      f'Имя пользователя: {message.from_user.first_name}\n'
                                      f'Фамилия пользователя: {message.from_user.last_name}\n'
                                      f'Юзернейм пользователя: {message.from_user.username}\n'

                     )
@bot.message_handler(commands=['test'])
def test(message):
    date = message.date + 10800
    date = datetime.datetime.utcfromtimestamp(date)
    bot.send_message(message.chat.id, date)

bot.polling()
