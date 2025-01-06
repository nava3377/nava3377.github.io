# emotion_detection.py
import numpy as np

def detect_emotion_rules(pitch, volume, tempo):
    # Example rule-based detection
    if np.mean(pitch) > 0.5 and np.mean(volume) > 0.2 and tempo > 120:
        return "Happy"
    elif np.mean(pitch) > 0.5 and np.mean(volume) < 0.3:
        return "Sad"
    else:
        return "Neutral"
