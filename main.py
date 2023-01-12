# Импортируем необходимые модули
import requests # для отправки HTTP-запросов
from datetime import datetime # для работы с датой и временем
import telebot # для работы с Telegram API
from telebot import types # для создания кнопок в Telegram
from auth_data import token # Импортируем токен для работы с Telegram из модуля auth_data

# Определяем константы для URL курсов BTC и ETH
BTC_URL = 'https://yobit.net/api/3/ticker/btc_usd'
ETH_URL = 'https://yobit.net/api/3/ticker/eth_usd'

# Функция для получения данных о курсе
def get_data(url):
    """
    Функция для получения данных о курсе
    """
    # Отправляем GET-запрос и получаем ответ в формате json
    req = requests.get(url)
    response = req.json()
    # Извлекаем из URL тикер валюты (btc_usd или eth_usd)
    ticker = url.split('/')[-1]
    # Если полученный тикер есть в ответе, возвращаем информацию о курсе
    if ticker in response:
        sell_price = response[ticker]['sell']
        if ticker == 'btc_usd':
            return f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nСтоимость BTC: {sell_price:.2f} $'
        elif ticker == 'eth_usd':
            return f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nСтоимость ETH: {sell_price:.2f} $'
    # Если тикер не найден, возвращаем сообщение об ошибке
    else:
        return f'Ошибка: неверный тикер валюты {ticker}'


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        markup = types.InlineKeyboardMarkup(row_width=1)
        item_1 = types.InlineKeyboardButton('BTC (bitcoin)', callback_data='btc')
        item_2 = types.InlineKeyboardButton('ETH (ethereum)', callback_data='eth')
        markup.add(item_1, item_2)

        bot.send_message(message.chat.id, 'Привет, Друг!\nНиже выбери курс какой криптовалюты ты хочешь узнать!', reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        if call.message:
            if call.data == 'btc':
                try:
                    course_message = get_data(BTC_URL)
                    bot.send_message(call.message.chat.id, course_message)
                except Exception as ex:
                    print(ex)
                    bot.send_message(
                        call.message.chat.id,
                        'Упс...Что-то произошло...'
                    )
            elif call.data == 'eth':
                try:
                    course_message = get_data(ETH_URL)
                    bot.send_message(call.message.chat.id, course_message)
                except Exception as ex:
                    print(ex)
                    bot.send_message(
                        call.message.chat.id,
                        'Упс...Что-то произошло...'
                    )

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text != '':
            bot.send_message(message.chat.id, 'Дружище, я умею только присылать актуальные курсы двух криптовалют :(')

    bot.polling()


if __name__ == '__main__':
    telegram_bot(token)


