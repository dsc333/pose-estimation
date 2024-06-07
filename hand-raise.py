import cv2
import mediapipe as mp
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start()

#Initialise Media Pipe Pose features
mp_pose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# Start endless loop to create video frame by frame
# Add details about video size and image post-processing to
# better identify bodies
while True:
    frame = picam2.capture_array()
    #flipped=cv2.flip(frame,flipCode=1)
    frame1 = cv2.resize(frame,(640,480))
    cv2.imshow("frame", frame1)
    rgb_img = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
    result = pose.process(rgb_img)
    print(result.pose_landmarks)

    # Uncomment below to see X,Y coordinate Details on single location
    # in this case the Nose Location.
    try:
        nose_x =  result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * 640
        nose_y = result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * 480
        l_wrist_y = result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y * 480
        print('Nose X,Y Coords are', nose_x, nose_y)
        print('Left write Y coordinate', l_wrist_y)
    except:
        pass

    # Draw the framework of body onto the processed image and then show it
    # in the preview window
    mpDraw.draw_landmarks(rgb_img,
                          result.pose_landmarks,
                          mp_pose.POSE_CONNECTIONS)
    if l_wrist_y < nose_y:
        cv2.putText(rgb_img, 'LEFT HAND RAISED',
                    (70, 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.imshow("frame",rgb_img)

    # At any point if the | q | is pressed on the keyboard then the
    # system will stop
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
