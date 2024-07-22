import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Example data
data = pd.DataFrame({
    'BMI': [22, 30, 25, 28],
    'BloodPressure': [80, 90, 85, 88],
    'BloodSugarProblems': [0, 1, 0, 1]
})

X = data[['BMI', 'BloodPressure']]
y = data['BloodSugarProblems']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')

with open(MODEL_PATH, 'wb') as f:
    pickle.dump(model, f)

