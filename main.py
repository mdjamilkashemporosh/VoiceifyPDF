import io
# import os
# from datetime import timedelta
# import pyttsx3
from PyPDF2 import PdfReader

from gtts import gTTS
from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.responses import StreamingResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_index():
    with open("./static/index.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/upload")
async def create_upload_file(file: UploadFile = File(...)):
    # Read the contents of the uploaded file as a byte stream

    contents = await file.read()

    # Create a PyPDF2 PdfReader object from the byte stream
    pdf_reader = PdfReader(io.BytesIO(contents))

    # Extract text from the PDF file
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Use gTTS to convert the text to an mp3 audio file
    language = "en"  # Change this to the appropriate language code
    tts = gTTS(text=text, lang=language)
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)

    # Save the audio file locally
    # filename = "output.mp3"
    # with open(filename, "wb") as f:
    #     f.write(audio_bytes.getbuffer())

    # Return the audio file as a response
    return StreamingResponse(audio_bytes, media_type="audio/mp3")
