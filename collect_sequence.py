import cv2
import mediapipe as mp
import numpy as np
import os

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

label = input("Masukkan label gesture: ").upper()
save_path = f"dataset/{label}"

os.makedirs(save_path, exist_ok=True)

cap = cv2.VideoCapture(0)

sequence = []
sequence_length = 30
counter = 0

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:

            data = []
            base_x = hand_landmarks.landmark[0].x
            base_y = hand_landmarks.landmark[0].y

            for lm in hand_landmarks.landmark:
                data.extend([lm.x - base_x, lm.y - base_y, lm.z])

            sequence.append(data)

            if len(sequence) == sequence_length:
                np.save(os.path.join(save_path, str(counter)), sequence)
                print(f"Saved sequence {counter}")
                sequence = []
                counter += 1

    cv2.imshow("Collect Sequence", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()