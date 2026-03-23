import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# ==============================
# LOAD DATASET
# ==============================
data = pd.read_csv("dataset.csv", header=None)

# ==============================
# PISAHKAN FITUR & LABEL
# ==============================
X = data.iloc[:, :-1]  # semua kolom kecuali terakhir
y = data.iloc[:, -1]   # kolom terakhir = label (A, B, dll)

# ==============================
# SPLIT DATA (TRAIN & TEST)
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==============================
# BUAT MODEL
# ==============================
model = RandomForestClassifier()

# training
model.fit(X_train, y_train)

# ==============================
# EVALUASI MODEL
# ==============================
accuracy = model.score(X_test, y_test)
print(f"Akurasi model: {accuracy * 100:.2f}%")

# ==============================
# SIMPAN MODEL
# ==============================
joblib.dump(model, "model.pkl")

print("Model berhasil disimpan sebagai model.pkl")