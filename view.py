from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from model import Model

class View:
    #Створюємо кнопки
    def create_crypto_markup(self) -> ReplyKeyboardMarkup:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        for crypto_name in Model.CRYPTO_NAME_TO_TICKER.keys():
            item_button = KeyboardButton(crypto_name)
            markup.add(item_button)
        return markup

    def get_welcome_message(self) -> str:
        return "Вітаю, користувачу. Оберіть криптовалюту."

    def get_price_message(self, crypto_name: str, price: float) -> str:
        return f"Ціна {crypto_name} до USDT становить {price}"
