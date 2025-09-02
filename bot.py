from telebot import TeleBot

BOT_TOKEN = "8277485140:AAERBu7ErxHReWZxcYklneU1wEXY--I_32c"  # Define token first

bot = TeleBot(BOT_TOKEN)  # Use token here
bot.remove_webhook()      # Prevents 409 conflict
