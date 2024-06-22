from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os
import shutil

from transcription import transcribe_audio_file
from summarization import summarize_text
from file_operations import save_files

app = FastAPI()

# Directory to save transcriptions and summaries
SAVE_DIR = "transcriptions"
os.makedirs(SAVE_DIR, exist_ok=True)

# Pydantic model for the response
class TranscriptionResponse(BaseModel):
    transcription: str
    summary: str
    timestamps: list

@app.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_audio_endpoint(file: UploadFile = File(...)):
    file_location = os.path.join(SAVE_DIR, file.filename)
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Transcription
    try:
        transcription, timestamps = transcribe_audio_file(file_location)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in transcription: {str(e)}")

    # Summarization
    try:
        summary = summarize_text(transcription)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in summarization: {str(e)}")

    # Save transcription, summary, and timestamps to files
    try:
        save_files(transcription, summary, timestamps)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving files: {str(e)}")

    return JSONResponse(content={
        "transcription": transcription,
        "summary": summary,
        "timestamps": timestamps
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
