from telebot import TeleBot
import requests
import json
import re

BOT_TOKEN = "8369296757:AAHQuwcxhkWKigYlwHVfUpKG19PejHWbgGY"
bot = TeleBot(BOT_TOKEN)

NUMBER_API = "https://glonova.in/croxty.php/?num="

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 *Welcome to OSINT Bot (VIP Style)*\n\nSend a 10-digit Phone Number to get details.",
        parse_mode="Markdown"
    )

@bot.message_handler(func=lambda m: m.text and m.text.strip())
def handle_input(message):
    number = message.text.strip().replace(" ", "")
    if re.match(r'^\d{10}$', number):
        fetch_number_info(message, number)
    else:
        bot.send_message(message.chat.id, "❌ Invalid input. Please send a valid 10-digit phone number.")

def fetch_number_info(message, number):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, f"📞 Scanning +91{number}...")

    try:
        res = requests.get(f"{NUMBER_API}{number}", timeout=15)
        text = res.text.encode('utf-8').decode('unicode_escape')
        data = json.loads(text)
        results = data.get("data", {}).get("Requested Number Results", [])

        if not results:
            return send_vip_not_found(message, number)

        r = results[0]
        requested_by = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name

        def get(k, default):
            v = r.get(k)
            if v is None or str(v).strip() == "" or str(v).strip().upper() == "N/A":
                return default
            return str(v).strip()

        msg = f"""🎯 *OSINT Intelligence Report*
┌─────────────────────────────────┐
│ 👤 Requested by: {requested_by}
│ 📱 Number: {number}
│ 📊 Status: Data Found ✅
│ 🔥𝘿𝙀𝙑🔥: @HACKER722727
└─────────────────────────────────┘

📋 *Detailed Information:*
👥 *Person 1:*
  📱 *Mobile Number:* `{get('📱 Mobile', number)}`
  👤 *Full Name:* `{get('👤 Name', 'Naam chhupa hua hai 😎')}`
  👨‍👦 *Father's Name:* `{get('👨‍👦 Father Name', 'Papa agent hai 🤫')}`
  🏠 *Complete Address:* `{get('🏠 Full Address', 'Google pe bhi nahi milta 😅')}`
  🆔 *Aadhar Number:* `{get('🆔 Aadhar Card', '4200-6969-1337 🔥')}`
  📧 *Email Address:* `{get('📧 Email', 'no_email@baba.in')}`
  📞 *Alternative Number:* `{get('📱 Alt Number', 'Nahi diya, attitude hai 😎')}`
  📡 *Network Provider:* `{get('📞 Sim/State', 'Pahadon se signal aa raha hai 😂')}`
"""
        bot.send_message(message.chat.id, msg, parse_mode="Markdown")

    except Exception as e:
        print("❌ Exception:", e)
        send_vip_not_found(message, number)

def send_vip_not_found(message, number):
    requested_by = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
    msg = f"""🎯 *OSINT Intelligence Report*
┌─────────────────────────────────┐
│ 👤 Requested by: {requested_by}
│ 📱 Number: {number}
│ 📊 Status: Not Found ❌
│ 🔥𝘿𝙀𝙑🔥: @HACKER722727
└─────────────────────────────────┘

📋 *Detailed Information:*
  👤 *Full Name:* `Unknown Legend 😎`
  👨‍👦 *Father:* `Baap bhi chhupa hua hacker 🥷`
  🏠 *Address:* `Mars pe bhi signal nahi hai 😆`
  📞 *Alt No:* `404_Not_Found 💔`
  📧 *Email:* `sach_mei_nahi@data.com`
  🆔 *Aadhar:* `0000-0000-0000 (Invisible Mode)`
  📡 *Network:* `Bhagwan Bharose 2G 🤣`
"""
    bot.send_message(message.chat.id, msg, parse_mode="Markdown")

print("🤖 Bot is running...")
bot.infinity_polling()
