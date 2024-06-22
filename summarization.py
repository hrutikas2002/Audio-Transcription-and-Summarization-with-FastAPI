from transformers import pipeline

# Load summarization model
try:
    summarization_model = pipeline("summarization", model="facebook/bart-large-cnn")
except Exception as e:
    raise RuntimeError(f"Failed to load summarization model: {str(e)}")

def summarize_text(text):
    try:
        summary = summarization_model(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        return summary
    except Exception as e:
        raise RuntimeError(f"Error in summarization: {str(e)}")
