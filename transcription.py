from transformers import pipeline

def transcribe_audio_file(audio_file_path: str):
    # Initialize the ASR pipeline
    whisper = pipeline('automatic-speech-recognition', model='openai/whisper-large')
    
    # Load the audio file
    with open(audio_file_path, 'rb') as audio_file:
        result = whisper(audio_file.read())
    
    # Extract transcription
    transcription = result['text']
    
    # Placeholder timestamps (modify as per your requirements)
    # Generate mock timestamps for each word
    words = transcription.split()
    timestamps = [{"word": word, "start_time": i, "end_time": i + 1} for i, word in enumerate(words)]
   

    return transcription, timestamps
