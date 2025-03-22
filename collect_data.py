import cv2
import numpy as np
import mediapipe as mp
import os
import csv

GESTURE_CLASSES = ['thumbs_up', 'peace_sign', 'fist', 'open_hand', 'pointing']

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

DATA_DIR = 'data'
os.makedirs(DATA_DIR, exist_ok=True)

gesture_id = 0
saving = False

def start_data_collection():
    global gesture_id, saving

    # Try to open the camera
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    print("\nPress 'N' to switch to next gesture.")
    print("Press 'S' to start saving landmarks.")
    print("Press 'Q' to quit.")

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

                if saving:
                    with open(os.path.join(DATA_DIR, f"{GESTURE_CLASSES[gesture_id]}.csv"), mode='a', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(landmarks)

                    cv2.putText(frame, "Saving...", (10, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.putText(frame, f"Gesture: {GESTURE_CLASSES[gesture_id]}", (10, 450),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.imshow("Data Collection", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('n'):
            gesture_id = (gesture_id + 1) % len(GESTURE_CLASSES)
            print(f"Switching to: {GESTURE_CLASSES[gesture_id]}")
        elif key == ord('s'):
            saving = not saving
            print(f"Saving: {saving}")

    cap.release()
    cv2.destroyAllWindows()

# For testing purposes, you can call the function directly:
if __name__ == "__main__":
    start_data_collection()
