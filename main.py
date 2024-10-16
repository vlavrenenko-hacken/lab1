from controller import Controller

TOKEN = "API_TOKEN"  # токен для Telegram бота

if __name__ == "__main__":
    controller = Controller(TOKEN)
    controller.start_bot()