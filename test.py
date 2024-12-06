from joblib import load
try:
    model = load('model.joblib')
    print("Model loaded successfully.")
except FileNotFoundError:
    print("Model file not found!")
