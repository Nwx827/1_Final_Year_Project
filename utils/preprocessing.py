# utils/preprocessing.py
import re
import pandas as pd

def clean_text(text):
    text = re.sub(r'<br\s*/?>', ' ', text)       # Remove <br />
    text = re.sub(r'[^a-zA-Z\s]', '', text)      # Remove special chars/numbers
    text = text.lower()                          # Lowercase
    text = re.sub(r'\s+', ' ', text).strip()     # Remove extra whitespace
    return text

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    df['review'] = df['review'].apply(clean_text)
    return df
