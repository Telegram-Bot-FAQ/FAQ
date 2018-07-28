from models import *
from telebot import TeleBot

bot = TeleBot('<token>')
# заготовка для реферальной ссылки
ref_link = 'https://telegram.me/{}?start={}'


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    # в случае с реферальными системами, нужно передать параметр
    # к команде /start=PARAM. Этот переметр будет передан боту
    # при вводе команды, например /start=1337
    # где 1337 -- ID пользователя который отправил приглашение
    # боту будет передано /start 1337
    # именно по этому мы разбиваем сообщение по пробелу
    # и смотрим есть ли там этот параметр
    splited = message.text.split()
    # проверяем наличие пользователя в базе данных
    if not Users.user_exists(user_id):
        # если его нет -- создаём
        Users.create_user(user_id)
        # проверяем перешел ли пользователь по реферальной ссылке
        if len(splited) == 2:
            # увеличиваем счетчик тому кто пригласил
            Users.increase_ref_count(splited[1])
    bot.reply_to(message, text='hello')


@bot.message_handler(commands=['get_my_link'])
def get_my_ref(message):
    # получаем username нашего бота и отпрявляем ссылку
    bot_name = bot.get_me().username
    bot.reply_to(message, text=ref_link.format(bot_name, message.chat.id))


@bot.message_handler(commands=['ref_count'])
def get_my_refs(message):
    # запрашиваем кол-во рефералов пользователя и отправляем ему
    count = Users.get_ref_count(message.chat.id)
    bot.reply_to(message, text=f'Count: {count}')


if __name__ == '__main__':
    bot.polling(none_stop=True)