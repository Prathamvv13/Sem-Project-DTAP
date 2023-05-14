import librosa
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import os
import resampy
import joblib

# Load the audio data and extract features
def extract_features(file_path):
    audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=20)
    mfccs_scaled = np.mean(mfccs.T, axis=0)
    return mfccs_scaled

# Define the directory path containing user folders
data_dir = 'C:/Users/Asus/Desktop/6th_sem_project/voice samples'

features = []
labels = []

# Traverse through the directory and extract features and labels
for user_folder in os.listdir(data_dir):
    user_folder_path = os.path.join(data_dir, user_folder)
    if os.path.isdir(user_folder_path):
        for file_name in os.listdir(user_folder_path):
            file_path = os.path.join(user_folder_path, file_name)
            if file_path.endswith('.flac' or '.wav'):
                extracted_features = extract_features(file_path)
                features.append(extracted_features)
                labels.append(user_folder)
                print("Done")

# print("Done")
X = np.array(features)
y = np.array(labels) # labels for each audio file

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = SVC(kernel='linear', probability=True)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'trained_model2.joblib')

# Test the model
y_pred = model.predict(X_test)
accuracy = np.mean(y_pred == y_test)
print("Accuracy:", accuracy)
# print("\n\n")
# # Assuming you have a new audio file path stored in 'new_file_path'

# # Extract features from the new input
# new_features = extract_features("C:/Users/Asus/Desktop/6th_sem_project/voice samples/4/4-14.flac")

# # Reshape the features to match the shape expected by the model
# new_features = new_features.reshape(1, -1)

# # Predict the output label for the new input
# new_prediction = model.predict(new_features)

# print("Prediction:", new_prediction)

