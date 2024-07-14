'''
Installation:
python3 -m venv --system-site-packages env
source env/bin/activate
pip3 install opencv-contrib-python
pip3 install mediapipe
'''

import cv2
import mediapipe as mp
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start()

# Initialise Media Pipe Pose features
mp_pose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# Width and height of resized frames from video feed
width = 640
height = 480

# Start endless loop to process video feed frame by frame
while True:
    frame = picam2.capture_array()
    frame1 = cv2.resize(frame,(width, height))
    cv2.imshow("frame", frame1)
    rgb_img = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
    result = pose.process(rgb_img)

    # If no landmarks are detected in current frame skip it
    if not result.pose_landmarks:
        continue
        
    print(result.pose_landmarks)

    try:
        nose_x =  result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * width
        nose_y = result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * height
        l_wrist_y = result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y * width
        print('Nose X,Y Coords are', nose_x, nose_y)
        print('Left write Y coordinate', l_wrist_y)
    except:
        pass

    # Draw the landmarks of body and then show it in the preview window
    mpDraw.draw_landmarks(rgb_img,
                          result.pose_landmarks,
                          mp_pose.POSE_CONNECTIONS)
    # if the wrist of left hand is higher than the nose
    # we'll output the message LEFT HAND RAISED
    if l_wrist_y < nose_y:
        cv2.putText(rgb_img, 'LEFT HAND RAISED',
                    (70, 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.imshow("frame",rgb_img)

    # Press the 'q' key to stop the program
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
