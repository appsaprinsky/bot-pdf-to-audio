import PyPDF3
import pyttsx3
import pdfplumber

file = 'dummy.pdf'
book = open(file, 'rb')
print(book)
pdfReader = PyPDF3.PdfFileReader(book)
pages = pdfReader.numPages

finalText = ""
 
with pdfplumber.open(file) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        finalText += text
# print(finalText)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices)
# for voice in voices:
#     if "english" in voice.languages[0].lower():
#         engine.setProperty('voice', voice.id)
#         break


engine.setProperty('rate', 160)

engine.save_to_file(finalText, 'dummy.mp3')
engine.runAndWait()        





