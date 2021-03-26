# from LiveFaceDetection.FaceDetection.livefacedetector import gen_frames
import numpy as np
import cv2
from flask import Flask,render_template,Response

app = Flask(__name__)
cap  = cv2.VideoCapture(0)

def gen_frames():
	while True:
		connect,frame = cap.read()
		if connect != True :
			print("camera connect not sucess")
			break
		else : 
			ret,buffer = cv2.imencode('.jpg',frame)
			frame = buffer.tobytes()
			yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
	app.run()