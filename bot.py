from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from speech_recognizer import AudioTranscriberSingleton

TOKEN = '6794189393:AAE6ZzH2wriksGIv7lvnwOi7odaKcjrZtB0'
audio_transcriber = AudioTranscriberSingleton()


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hola, soy tu bot de Telegram. ¡Envíame mensajes!')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def handle_voice(update: Update, context: CallbackContext) -> None:
    voice = update.message.voice
    duration = voice.duration
    file_id = voice.file_id

    voice_file = context.bot.get_file(file_id)
    voice_file.download("voice_messages/message.ogg")
    text = audio_transcriber.transcribe_audio("voice_messages/message.ogg")

    update.message.reply_text(f"Haz dicho {text}")

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