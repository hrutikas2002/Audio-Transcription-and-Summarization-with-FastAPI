# Audio Transcription and Summarization API

## Project Description

This project provides an API for transcribing audio files into text and summarizing the transcriptions. It uses state-of-the-art machine learning models from the `transformers` library.

## Features

- Upload an audio file and get a transcription.
- Get a summary of the transcribed text.
- Receive word-level timestamps in the transcription.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- transformers
- pydantic
- shutil
- ffmpeg (for audio processing)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Install FFmpeg:
    - Go to the [FFmpeg download page](https://ffmpeg.org/download.html).
    - Download the appropriate version for your operating system.
    - Follow the instructions to install FFmpeg and add it to your system's PATH.

## Usage

1. Start the FastAPI server:
    ```bash
    uvicorn app:app --reload
    ```

2. Access the API documentation:
    Open your web browser and go to `http://127.0.0.1:8000/docs` to view the interactive API documentation.

3. Upload an audio file:
    - Use the `/transcribe` endpoint to upload an audio file and receive the transcription, summary, and timestamps.

## API Endpoints

- `POST /transcribe`: Upload an audio file and get a transcription, summary, and word-level timestamps.

Directory Structure in VSCode:
.
├── app.py                   # Main FastAPI application
├── transcription.py         # Transcription logic
├── summarization.py         # Summarization logic
├── file_operations.py       # File operations logic
├── requirements.txt         # List of required Python packages
├── transcriptions/          # To store the transcription and summary files generated for each audio file processed by the API.
