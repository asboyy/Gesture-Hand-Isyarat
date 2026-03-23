import joblib
import csv
import cv2
import mediapipe as mp
import time
from collections import Counter
from textblob import TextBlob
from gtts import gTTS
from playsound import playsound
import os

# ==============================
# TEXT TO SPEECH (GOOGLE) 🇮🇩
# ==============================
def speak(text):
    try:
        tts = gTTS(text=text, lang='id')  # bahasa Indonesia
        filename = "temp.mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except:
        print("Gagal memutar suara")

# ==============================
# VARIABEL GLOBAL
# ==============================
word = ""
sentence = ""
last_letter = ""
last_time = 0
delay = 1

current_label = None
recording = False
last_save_time = 0

gesture_buffer = []

# ==============================
# INIT MEDIAPIPE
# ==============================
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1)

# ==============================
# LOAD MODEL
# ==============================
model = joblib.load("model.pkl")

# ==============================
# INIT CAMERA
# ==============================
cap = cv2.VideoCapture(0)

# ==============================
# DETEKSI TANGAN
# ==============================
def is_hand_open(hand_landmarks):
    tips = [8, 12, 16, 20]
    open_fingers = 0

    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            open_fingers += 1

    return open_fingers

# ==============================
# SIMPAN DATASET
# ==============================
def save_landmarks(hand_landmarks, label):
    data = []

    base_x = hand_landmarks.landmark[0].x
    base_y = hand_landmarks.landmark[0].y

    for lm in hand_landmarks.landmark:
        data.extend([lm.x - base_x, lm.y - base_y, lm.z])

    with open("dataset.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data + [label])

# ==============================
# PREDIKSI
# ==============================
def predict_gesture(hand_landmarks):
    data = []

    base_x = hand_landmarks.landmark[0].x
    base_y = hand_landmarks.landmark[0].y

    for lm in hand_landmarks.landmark:
        data.extend([lm.x - base_x, lm.y - base_y, lm.z])

    prediction = model.predict([data])
    return prediction[0]

# ==============================
# SPELL CORRECTION (AI)
# ==============================
def correct_word(w):
    try:
        return str(TextBlob(w).correct())
    except:
        return w

# ==============================
# LOOP UTAMA
# ==============================
ESC_KEY = 27
last_spoken_word = ""

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    key = cv2.waitKey(1) & 0xFF

    # ==========================
    # CONTROL
    # ==========================
    if key >= ord('a') and key <= ord('z'):
        current_label = chr(key).upper()
        print(f"Label: {current_label}")

    if key == ord(' '):
        recording = not recording
        print("Recording:", recording)

    if key == ord('c'):
        word = ""
        print("Reset word")

    if key == ord('s'):
        word += " "

    if key == ESC_KEY:
        print("Keluar ESC")
        break

    # tekan 'v' untuk baca seluruh kalimat
    if key == ord('v'):
        speak(sentence)

    # ==========================
    # DETEKSI
    # ==========================
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:

            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            gesture = predict_gesture(hand_landmarks)
            gesture_buffer.append(gesture)

            if len(gesture_buffer) > 5:
                gesture_buffer.pop(0)

            most_common = Counter(gesture_buffer).most_common(1)[0][0]

            cv2.putText(img, f"Gesture: {most_common}", (10,100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

            # ======================
            # AUTO WORD + AUTO SPEAK 🔥
            # ======================
            current_time = time.time()

            if most_common != last_letter:
                if current_time - last_time > delay:
                    word += most_common
                    last_letter = most_common
                    last_time = current_time

                    # 🔊 AUTO SPEAK (tanpa ENTER)
                    if word != last_spoken_word:
                        speak(word)
                        last_spoken_word = word

            # OPEN / CLOSED
            fingers = is_hand_open(hand_landmarks)
            if fingers >= 4:
                cv2.putText(img, "OPEN", (10,50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            else:
                cv2.putText(img, "CLOSED", (10,50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

            # AUTO SAVE
            if recording and current_label is not None:
                if time.time() - last_save_time > 0.2:
                    save_landmarks(hand_landmarks, current_label)
                    last_save_time = time.time()
                    print(f"Saving {current_label}...")

    # ==========================
    # AI SMART SENTENCE
    # ==========================
    corrected = correct_word(word)
    sentence = corrected

    # ==========================
    # UI
    # ==========================
    cv2.putText(img, f"Word: {word}", (10,150),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)

    cv2.putText(img, f"AI: {corrected}", (10,200),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.putText(img, f"Sentence: {sentence}", (10,250),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)

    cv2.putText(img, "ESC=Exit | SPACE=Record | V=Speak", (10,300),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

    cv2.imshow("Hand Gesture AI PRO", img)

# ==============================
# RELEASE
# ==============================
cap.release()
cv2.destroyAllWindows()