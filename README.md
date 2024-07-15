# Pose Estimation

Detects body landmark positions in real-time from an RPI video feed.  
Outputs an appropriate message when subject in video feed raises their
left hand.  

**Installation Instructions:**
1. git clone https://github.com/dsc333/pose-estimation
2. cd pose-estimation
3. python3 -m venv --system-site-packages env
4. source env/bin/activate
5. pip3 install opencv-contrib-python
6. pip3 install mediapipe
7. python3 hand-raise.py
8. Press 'q' to quit the program
9. Type: deactivate when done
