
import io
import pyttsx3
import PyPDF3
import logging
import asyncio
from gtts import gTTS



file = 'sample_eng.pdf'
book = open(file, 'rb')
pdfReader = PyPDF3.PdfFileReader(book)
finalText =  pdfReader.getPage(0).extractText()

print(f"Printing...{finalText}")
engine = pyttsx3.init()

tts = gTTS(text=finalText, lang='en', slow=False)
audio_file = io.BytesIO()
tts.write_to_fp(audio_file)
audio_file.seek(0)

 