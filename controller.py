from telebot import TeleBot
from model import Model
from view import View

TOKEN = "API_TOKEN" # токен для Телеграм бота

class Controller:
    def __init__(self, token):
        self.bot = TeleBot(token)
        self.model = Model()
        self.view = View()
        self.setup_handlers()

    # Налаштування обробників команд, через start
    def setup_handlers(self):
        @self.bot.message_handler(commands=['start'])
        def send_welcome(message):
            markup = self.view.create_crypto_markup()
            self.bot.send_message(message.chat.id, self.view.get_welcome_message(), reply_markup=markup)

        # Запит на ціну криптовалюти 
        @self.bot.message_handler(func=lambda message: message.text in Model.CRYPTO_NAME_TO_TICKER.keys())
        def send_price(message):
            crypto_name = message.text
            ticker = Model.CRYPTO_NAME_TO_TICKER[crypto_name]
            price = self.model.get_price_by_ticker(ticker)
            self.bot.send_message(message.chat.id, self.view.get_price_message(crypto_name, price))

    # Запуск серверу бота
    def start_bot(self):
        self.bot.infinity_polling()
