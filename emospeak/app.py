from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

import re
import numpy as np
import librosa

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@localhost/nava'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('login.html')
@app.route('/home')
def home():
    return render_template('recorded_audio.html')

@app.route('/home1')
def home1():
    return render_template('live_audio.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username_data = request.form['username']
        email_data = request.form['email']
        password_data = request.form['password']
        confirm_password_data = request.form['confirmpassword']

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email_data):
            flash('Invalid email address.', 'error')
        elif password_data != confirm_password_data:
            flash('Passwords do not match.', 'error')
        else:
            hashed_password = generate_password_hash(password_data, method='pbkdf2:sha256')
            new_user = User(name=username_data, email=email_data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('User created successfully!', 'success')
            return redirect(url_for('signup'))

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_data = request.form['email']
        password_data = request.form['password']

        user = User.query.filter_by(email=email_data).first()

        if user and check_password_hash(user.password, password_data):
            flash(f'Login successful. Welcome, {user.name}!', 'success')
            return render_template('home.html')

        else:
            flash('Invalid email or password.', 'error')

    return render_template('login.html')

@app.route('/forgetpassword', methods=['GET', 'POST'])
def forgetpassword():
    if request.method == 'POST':
        username_data = request.form['username']
        new_password_data = request.form['password']
        confirm_password_data = request.form['confirmpassword']

        user = User.query.filter_by(name=username_data).first()

        if user:
            if new_password_data == confirm_password_data:
                user.password = generate_password_hash(new_password_data, method='pbkdf2:sha256')

                db.session.commit()
                flash('Password reset successful!', 'success')
                return redirect(url_for('login'))
            else:
                flash('Passwords do not match.', 'error')
        else:
            flash('User not found.', 'error')

    return render_template('forgetpassword.html')
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
    app.run(debug=True)
