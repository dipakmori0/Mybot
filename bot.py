from telebot import TeleBot

BOT_TOKEN = "8277485140:AAERBu7ErxHReWZxcYklneU1wEXY--I_32c"
bot = TeleBot(BOT_TOKEN)
bot.remove_webhook()  # Prevents 409 conflict

print("🤖 Bot is starting...")
bot.infinity_polling()
