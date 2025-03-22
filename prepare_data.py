import os
import numpy as np

# Define gesture classes
gesture_classes = ['thumbs_up', 'peace_sign', 'fist', 'open_hand', 'pointing']

# Load existing data
data = []
labels = []

for idx, gesture in enumerate(gesture_classes):
    gesture_path = f'data/{gesture}'
    if os.path.exists(gesture_path):
        for file in os.listdir(gesture_path):
            file_path = os.path.join(gesture_path, file)
            sample = np.load(file_path)
            data.append(sample)
            labels.append(idx)

# Convert to numpy arrays
X = np.array(data)
y = np.array(labels)

# Save processed data
np.save('data/X.npy', X)
np.save('data/y.npy', y)

print("Data prepared and saved to 'data/X.npy' and 'data/y.npy'")
