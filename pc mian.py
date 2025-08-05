from flask import Flask
import pyttsx3
import time

app = Flask(__name__)
last_spoken_time = 0

@app.route('/motion')
def motion_detected():
    global last_spoken_time
    now = time.time()
    
    if now - last_spoken_time < 5:
        return "Too soon"

    last_spoken_time = now
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say("Someone is at the door")
    engine.runAndWait()
    return "Motion received"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
