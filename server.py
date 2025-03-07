from flask import Flask
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# استبدل 'YOUR_TELEGRAM_BOT_TOKEN' بالتوكن الخاص ببوتك
TOKEN = '5260047648:AAEi6qjEL3_egn3JCTgXGNHMzfDvkBtF6Ss'

# تعريف أمر /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحبًا! أنا بوت تلجرام يعمل على Glitch.')

# تعريف أمر /echo
def echo(update: Update, context: CallbackContext) -> None:
    text = ' '.join(context.args)  # النص الذي يكتبه المستخدم بعد /echo
    update.message.reply_text(text)

# تشغيل البوت
def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    # إضافة الأوامر
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("echo", echo))

    # بدء الاستقبال
    updater.start_polling()
    updater.idle()

# تشغيل خادم Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running!"

if __name__ == '__main__':
    # تشغيل البوت
    main()
    # تشغيل خادم Flask
    app.run(host='0.0.0.0', port=3000)
