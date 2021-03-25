import pyttsx3
import PyPDF2
# PDF File
Book = open('SamplePDF','rb')
# PDF Reader
PdfReader = PyPDF2.PdfFileReader(Book)
# Text to Speech
TextToSpeech = pyttsx3.init()
# Get Specific page
page = PdfReader.getPage(31)
# Page Text
text = page.extractText()
# Speech Text
TextToSpeech.say(text)
TextToSpeech.runAndWait()
