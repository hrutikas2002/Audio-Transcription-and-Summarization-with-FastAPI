import os
import json
from datetime import datetime

SAVE_DIR = "transcriptions"
os.makedirs(SAVE_DIR, exist_ok=True)

def save_files(transcription, summary, timestamps):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        transcription_file = os.path.join(SAVE_DIR, f"transcription_{timestamp}.txt")
        summary_file = os.path.join(SAVE_DIR, f"summary_{timestamp}.txt")
        timestamps_file = os.path.join(SAVE_DIR, f"timestamps_{timestamp}.json")

        with open(transcription_file, "w") as f:
            f.write(transcription)
        
        with open(summary_file, "w") as f:
            f.write(summary)
        
        with open(timestamps_file, "w") as f:
            json.dump(timestamps, f)

        return transcription_file, summary_file, timestamps_file
    except Exception as e:
        raise RuntimeError(f"Error saving files: {str(e)}")
