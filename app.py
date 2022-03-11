from asyncore import dispatcher
from telegram import (
    Update
)

from telegram.ext import (
    Filters,
    Updater,
    MessageHandler,
    CommandHandler,
    CallbackContext

)


WEBHOOK_URL = "104.197.6.61"
WEBHOOK_HOST = "0.0.0.0"
WEBHOOK_PORT = "8443"
CERT_PATH = "./url_cert.pem"
KEY_PATH = "./url_private.key"

API_TOKEN = "5063316173:AAGUZtfr1OQ9K-mY3w_pl81gOpj-6KKKBIg"
updater = Updater(API_TOKEN)
dp = updater.dispatcher

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi!")

def echo(update: Update, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id, update.message.text)

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.all & ~Filters.command, echo))

updater.start_webhook(
    webhook_url=WEBHOOK_URL,
    listen=WEBHOOK_HOST,
    port=WEBHOOK_PORT,
    # cert=CERT_PATH,
    # key=KEY_PATH
)