import cv2
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model
import pyttsx3

# Load trained model
model = load_model('model/model.h5')

# Define gesture classes (in the same order as during training)
GESTURE_CLASSES = ['thumbs_up', 'peace_sign', 'fist', 'open_hand', 'pointing']

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Initialize text-to-speech
engine = pyttsx3.init()

# Function to speak gesture
def speak(gesture):
    engine.say(f"Detected {gesture}")
    engine.runAndWait()

# Function to start gesture recognition
def start_gesture_recognition():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("\nPress 'Q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                landmarks = []
                for landmark in hand_landmarks.landmark:
                    landmarks.extend([landmark.x, landmark.y, landmark.z])

                # Reshape data for prediction
                input_data = np.array(landmarks).reshape(1, -1)

                # Make a prediction using the trained model
                prediction = model.predict(input_data)
                gesture_id = np.argmax(prediction)
                confidence = np.max(prediction)

                if confidence > 0.7:  # Minimum confidence threshold
                    gesture_name = GESTURE_CLASSES[gesture_id]
                    
                    # Display the predicted gesture
                    cv2.putText(frame, f"{gesture_name} ({confidence:.2f})", (10, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                    # Speak the gesture name
                    speak(gesture_name)

        cv2.imshow("Sign Language Recognition", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# For direct testing:
if __name__ == "__main__":
    start_gesture_recognition()
