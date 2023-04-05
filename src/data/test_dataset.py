import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import sys

current = os.path.dirname(os.path.realpath(__file__)) # getting the name of the directory where this file is present.
parent = os.path.dirname(current) # Getting the parent directory name where the current directory is present.
sys.path.append(parent) # adding the parent directory to the sys.path.

from utils.index import mp_holistic, mediapipe_detection, extract_keypoints, draw_landmarks
# import time
# import mediapipe as mp

actions = np.array(["test_1",'test2'])

# Path for exported data (numpy arrays)
DATA_PATH = os.path.join(r'data\test') 

# Thirty videos worth of data
no_sequences = 30

# Videos are going to be 30 frames in length
sequence_length = 30

for action in actions: 
    for sequence in range(no_sequences):
        try: 
            os.makedirs(os.path.join(DATA_PATH, action, str(sequence)))
        except:
            pass
        
cap = cv2.VideoCapture(0)
# Set mediapipe model 
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:

    # Add pause flag
    pause = False
    
    # NEW LOOP
    # Loop through actions
    for action in actions:
        # Loop through sequences aka videos
        for sequence in range(no_sequences):
            # Loop through video length aka sequence length
            for frame_num in range(sequence_length):
                
                # Add pause logic
                while pause:
                    key = cv2.waitKey(30)
                    # Press 'r' to resume
                    if key == ord('r'):
                        pause = False
                    # Press 'q' to quit
                    elif key == ord('q'):
                        break
                
                # Read feed
                ret, frame = cap.read()
                frame = cv2.flip(frame, 1)

                # Make detections
                image, results = mediapipe_detection(frame, holistic)

                # Draw landmarks
                draw_landmarks(image, results)
                
                # NEW Apply wait logic
                if frame_num == 0: 
                    cv2.putText(image, 'STARTING COLLECTION', (120,200), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 4, cv2.LINE_AA)
                    cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15,12), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                    # Show to screen
                    cv2.imshow('OpenCV Feed', image)
                    cv2.waitKey(2000)
                else: 
                    cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15,12), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                    # Show to screen
                    cv2.imshow('OpenCV Feed', image)
                
                # NEW Export keypoints
                keypoints = extract_keypoints(results)
                npy_path = os.path.join(DATA_PATH, action, str(sequence), str(frame_num))
                np.save(npy_path, keypoints)

                # Break gracefully
                key = cv2.waitKey(10)
                if key == ord('q'):
                    break
                # Press 'p' to pause
                elif key == ord('p'):
                    pause = True
                    
    cap.release()
    cv2.destroyAllWindows()