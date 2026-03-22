import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1)

cap = cv2.VideoCapture(0)

# 🔧 fungsi deteksi jari
def is_hand_open(hand_landmarks):
    tips = [8, 12, 16, 20]
    open_fingers = 0

    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            open_fingers += 1

    return open_fingers

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:

            # 🖐️ gambar tangan
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # 🔥 TAMBAHAN LOGIKA DI SINI
            fingers = is_hand_open(hand_landmarks)

            if fingers >= 4:
                cv2.putText(img, "OPEN HAND", (10,50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            else:
                cv2.putText(img, "CLOSED HAND", (10,50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow("Hand Tracking", img)

    # tekan q untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()