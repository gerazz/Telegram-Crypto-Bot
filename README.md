# **Telegram Crypto Bot** :money_with_wings:

Это простой бот Telegram, который позволяет пользователям проверять текущие цены продажи биткойнов (BTC) и Ethereum (ETH) в долларах США. Бот использует Yobit API для получения цен и библиотеку телеботов для взаимодействия с Telegram API.

## **Начало**
____

1. Клонируйте этот репозиторий на свой локальный компьютер, используяgit clone https://github.com/YOUR_USERNAME/Telegram-Crypto-Bot.git
2. Установите необходимые зависимости, запустив 
   ```python
   pip install -r requirements.txt
   ```
3. Создайте нового бота в Telegram и получите его токен.
4. Создайте новый модуль с именем auth_data.pyв корневом каталоге проекта и добавьте в него следующую строку кода:
   ```python
   token = 'YOUR_TELEGRAM_BOT_TOKEN'
   ```
5. Запустите программу с помощью следующей команды: 
   ```python
   python main.py
   ```
6. Запустите бота, отправив /start команду в чат с ботом


## **Применение**
___
Как только вы запустите бота, вам будут представлены две кнопки — одна для BTC и одна для ETH. При выборе одной из этих кнопок будет отправлено сообщение с текущей ценой продажи выбранной валюты в долларах США.


## **Сделано при помощи**
___
· [Python](https://www.python.org/) — язык программирования

· [telebot](https://pypi.org/project/pyTelegramBotAPI/) — оболочка Telegram Bot API для Python

· [requests](https://requests.readthedocs.io/en/latest/) - HTTP-библиотека для Python


## **Авторы**
Gera Zaharchenko - [GeraZz](https://github.com/gerazz) - Github :zzz: