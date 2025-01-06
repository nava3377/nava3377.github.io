import numpy as np
from flask import Flask, render_template, request
import librosa

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    # Get the uploaded audio file
    audio_file = request.files['audio']
    audio_path = 'uploaded_audio.wav'
    audio_file.save(audio_path)

    # Load the audio file
    audio_data, sample_rate = librosa.load(audio_path)

    # Compute pitch, volume, and tempo
    pitch = librosa.piptrack(y=audio_data, sr=sample_rate)
    volume = librosa.feature.rms(y=audio_data)
    tempo = librosa.beat.tempo(y=audio_data, sr=sample_rate)

    # Convert pitch and volume to NumPy arrays
    pitch = np.array(pitch)
    volume = np.array(volume)

    # Reshape pitch and volume arrays to have the same number of dimensions
    pitch = pitch.reshape(-1, 1)
    volume = volume.reshape(-1, 1)

    # Assuming tempo is a single value or a 1D array, reshaping it to a 2D column vector
    tempo = np.array(tempo).reshape(-1, 1)

    # Now, concatenate the reshaped arrays
    combined_features = np.concatenate((pitch, volume, tempo), axis=0)

    # Rule-based emotion detection
    emotion = detect_emotion_rules(pitch, volume, tempo)

    return render_template('result.html', emotion=emotion)

def detect_emotion_rules(pitch, volume, tempo):
    # Example rule-based detection
    if np.mean(pitch) > 0.5 and np.mean(volume) > 0.2 and tempo > 120:
        return "Happy"
    elif np.mean(pitch) > 0.5 and np.mean(volume) < 0.3:
        return "Sad"
    else:
        return "Neutral"

if __name__ == '__main__':
    app.run(port=5001,debug=True)
 