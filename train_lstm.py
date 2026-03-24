import numpy as np
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

DATA_PATH = "dataset"
labels = os.listdir(DATA_PATH)

X = []
y = []

for idx, label in enumerate(labels):
    for file in os.listdir(os.path.join(DATA_PATH, label)):
        data = np.load(os.path.join(DATA_PATH, label, file))
        X.append(data)
        y.append(idx)

X = np.array(X)
y = np.array(y)

# ======================
# MODEL LSTM
# ======================
model = Sequential()
model.add(LSTM(64, return_sequences=True, input_shape=(30, 63)))
model.add(LSTM(128))
model.add(Dense(64, activation='relu'))
model.add(Dense(len(labels), activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(X, y, epochs=20)

model.save("model_lstm.h5")

np.save("labels.npy", labels)

print("Model selesai dilatih!")