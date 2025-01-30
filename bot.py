from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7889429106:AAEa73H5yR4kdVHj3jYevxgeFlUT15wviAQ"  # Yahan apna bot token daalein
OWNER_ID = "@Anshtrader12"  # Owner ka Telegram username (not link)
VIP_CHANNEL = "https://t.me/your_vip_channel_link"  # VIP Channel ka actual link
PUBLIC_CHANNEL = "https://t.me/learnansh87"  # Public Channel ka link

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    
    # Welcome Image (replace with your image URL)
    image_url = "https://your-image-url.com/image.jpg"  # Yahan apni image ka URL daalein
    context.bot.send_photo(chat_id=chat_id, photo=image_url)

    # Welcome Message
    welcome_text = "👋 Welcome to our bot! Click the buttons below to contact the owner, join the VIP channel, or visit our public channel."

    # Buttons
    keyboard = [
        [InlineKeyboardButton("👤 Contact Owner", url=f"tg://user?id={OWNER_ID}")],  
        [InlineKeyboardButton("🌟 VIP Channel", url=VIP_CHANNEL)],  
        [InlineKeyboardButton("📢 Public Channel", url=PUBLIC_CHANNEL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send Message
    context.bot.send_message(chat_id=chat_id, text=welcome_text, reply_markup=reply_markup)

def vip_channel(update: Update, context: CallbackContext):
    # VIP Channel Message
    vip_message = """
🅱️🔡🔡🔡 🔡🔡🔡

😮😕😕😄 😬

✔️JOIN NOW✔️

😬JUST CREATE NEW QUOTEX ACCOUNT THROUGH THIS LINK -:

😬https://broker-qx.pro/sign-up/?lid=1170252

🤨DEPOSIT MINIMUM 5000RS (50$)

🔥SEND ME YOUR TRADER ID HERE-: @Anshtrader12

👑Then i will share you 🔑 key & start your earning😴 +learning🫣

❓𝗗𝗜𝗥𝗘𝗖𝗧𝗟𝗬 𝗧𝗔𝗟𝗞 𝗪𝗜𝗧𝗛 𝗠𝗘 𝗠𝗦𝗚 𝗛𝗘𝗥𝗘 -: @Anshtrader12

🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽
    """
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=vip_message)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("vip_channel", vip_channel))  # VIP Channel button ke liye

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
