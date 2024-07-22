import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'base', 'model.pkl')

def load_model():
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

def predict_blood_sugar(bmi, blood_pressure):
    prediction = model.predict_proba([[bmi, blood_pressure]])[0][1]*100
    if prediction > 60:
        print("You are at High Risk")
    return prediction
