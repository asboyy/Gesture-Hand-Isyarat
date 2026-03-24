import importlib
import sys


REQUIRED_MODULES = [
    ("cv2", "opencv-contrib-python"),
    ("mediapipe", "mediapipe"),
    ("tensorflow", "tensorflow"),
    ("google.protobuf", "protobuf"),
    ("numpy", "numpy"),
    ("pandas", "pandas"),
    ("sklearn", "scikit-learn"),
    ("joblib", "joblib"),
    ("textblob", "textblob"),
    ("gtts", "gTTS"),
    ("playsound", "playsound"),
]


def main() -> int:
    print(f"Python: {sys.version.split()[0]}")
    failed = []

    for module_name, package_name in REQUIRED_MODULES:
        try:
            module = importlib.import_module(module_name)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {package_name:<20} -> {version}")
        except Exception as exc:
            failed.append((package_name, exc))
            print(f"[FAIL] {package_name:<20} -> {exc}")

    if failed:
        print("\nEnvironment belum siap.")
        return 1

    print("\nEnvironment siap dipakai.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
