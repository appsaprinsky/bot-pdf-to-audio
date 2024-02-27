from telegram.ext import *
import io
import pyttsx3
import PyPDF3
from gtts import gTTS
import os



print('Starting a bot....')

async def start_commmand(update, context):
    await update.message.reply_text('Welcome to the PDF to Audio bot! Send me a PDF file and I will convert it to audio for you.')


async def convert_pdf_to_audio(update, context):
    if update.message.document:
        file_info = update.message.document
        file_name = file_info.file_name
        file_size = file_info.file_size
        file_id = file_info.file_id
        await update.message.reply_text(f'Receiving {file_name} ({file_size} bytes)')
        new_file = await context.bot.get_file(file_id)
        downloaded_file = io.BytesIO(await new_file.download_as_bytearray())

        pdf_file = PyPDF3.PdfFileReader(downloaded_file)
        finalText =  pdf_file.getPage(0).extractText()
        print(f"Printing...{finalText}")
        engine = pyttsx3.init()

        tts = gTTS(text=finalText, lang='en', slow=False)
        audio_file = io.BytesIO()
        tts.write_to_fp(audio_file)
        audio_file.seek(0)
        await context.bot.send_voice(chat_id=update.effective_chat.id, voice=audio_file)
        await context.bot.send_audio(chat_id=update.effective_chat.id, voice=audio_file)



if __name__ == '__main__':
    application = Application.builder().token(os.environ['TELEGRAM_BOT_TOKEN']).build()
    application.add_handler(CommandHandler('start', start_commmand))
    application.add_handler(MessageHandler(filters.Document.ALL, convert_pdf_to_audio))
    application.run_polling(1.0)