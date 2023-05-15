import joblib
import librosa
import numpy as np

# Load the saved model
model = joblib.load('trained_model2.joblib')

# Load the audio data and extract features
def extract_features(file_path):
    audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=20)
    mfccs_scaled = np.mean(mfccs.T, axis=0)
    return mfccs_scaled

# Extract features from the new input
new_features = extract_features("C:/Users/Asus/Desktop/6th_sem_project/test/1-20.flac")

# Reshape the features to match the shape expected by the model
new_features = new_features.reshape(1, -1)

# Use the loaded model for prediction
new_prediction = model.predict(new_features)

print("Prediction:", new_prediction)

