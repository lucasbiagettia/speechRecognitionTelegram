from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = ''

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hola, soy tu bot de Telegram. ¡Envíame mensajes!')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def handle_voice(update: Update, context: CallbackContext) -> None:
    voice = update.message.voice
    duration = voice.duration
    file_id = voice.file_id

    voice_file = context.bot.get_file(file_id)
    voice_file.download(f"voice_messages/{file_id}.ogg")

    update.message.reply_text(f"Recibí un mensaje de voz de {duration} segundos. ID: {file_id}")

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    dp.add_handler(MessageHandler(Filters.voice, handle_voice))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()