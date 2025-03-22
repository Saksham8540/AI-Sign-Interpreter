import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Define gesture classes
gesture_classes = ['thumbs_up', 'peace_sign', 'fist', 'open_hand', 'pointing']
data = []
labels = []

# Load data from CSV files
for i, gesture in enumerate(gesture_classes):
    df = pd.read_csv(f'data/{gesture}.csv')
    data.append(df.values)
    labels.append(np.full((df.shape[0],), i))  # Create label array for each class

# Combine all data and labels
X = np.concatenate(data)
y = np.concatenate(labels)

# Shuffle the data to avoid overfitting
indices = np.arange(X.shape[0])
np.random.shuffle(indices)
X = X[indices]
y = y[indices]

# Build the model
model = Sequential([
    Dense(128, activation='relu', input_shape=(X.shape[1],)),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(len(gesture_classes), activation='softmax')  # Output layer for classification
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=20, batch_size=32)

# Save the model
model.save('model/model.h5')
print("Model saved to 'model/model.h5'")
