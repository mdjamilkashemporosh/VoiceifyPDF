# Dependency
import pyttsx3
import PyPDF2
from gtts import gTTS


# PDF File
Book = open('SamplePDF.pdf','rb')


# PDF Reader
PdfReader = PyPDF2.PdfFileReader(Book)


# Pages 
# PagesNumber = PdfReader.numPages
# print(PagesNumber)


# Text to Speech Engine
TextToSpeechEngine = pyttsx3.init()


# Get Specific Page
page = PdfReader.getPage(0)


# Specific Page Text
text = page.extractText()


# Speech Text
# TextToSpeechEngine.say(text)
# TextToSpeechEngine.runAndWait()


# Save As Audio 
tts = gTTS(text=text, lang='en')
tts.save("saved_file.mp3")
print("File saved!")

