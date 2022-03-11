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
from torch import USE_RTLD_GLOBAL_WITH_LIBTORCH


WEBHOOK_URL = "104.197.6.61"
WEBHOOK_LISTEN = "0.0.0.0"
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
    listen=WEBHOOK_LISTEN,
    port=WEBHOOK_PORT,
    url_path=API_TOKEN,
    webhook_url=f"https://{WEBHOOK_URL}:{WEBHOOK_PORT}/{API_TOKEN}",
    cert=CERT_PATH,
    key=KEY_PATH
)
