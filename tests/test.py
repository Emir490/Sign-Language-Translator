import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import time
import mediapipe as mp
from keras.models import load_model
from src.utils.index import actions, extract_keypoints, mediapipe_detection, draw_landmarks, mp_holistic

model = load_model('model')

print(len(actions))

colors = [(245, 117, 16), (117, 245, 16), (16, 117, 245)]

#, (245, 16, 117), (117, 16, 245), (16, 245, 117), (245, 245, 16), (245, 16, 245), (16, 245, 245), (245, 117, 245), (117, 245, 117), (117, 117, 245), (245, 117, 117), (117, 245, 245), (16, 16, 245), (16, 245, 16), (245, 16, 16), (245, 117, 117), (117, 117, 16), (117, 16, 117), (117, 16, 16), (16, 117, 117), (245, 245, 117), (245, 117, 245), (117, 245, 117), (117, 117, 117), (245, 245, 245)

def prob_viz(res, actions, input_frame, colors):
    output_frame = input_frame.copy()
    for num, prob in enumerate(res):
        x1, y1 = 0, 60 + num * 20
        x2, y2 = int(prob * 100), 80 + num * 20
        cv2.rectangle(output_frame, (x1, y1), (x2, y2), colors[num], -1)
        cv2.putText(output_frame, actions[num], (0, y2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    return output_frame

# 1. New detection variables
sequence = []
sentence = []
threshold = 0.8

cap = cv2.VideoCapture(0)
# Set mediapipe model 
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():

        # Read feed
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        # Make detections
        image, results = mediapipe_detection(frame, holistic)
        #print(results)
        
        # Draw landmarks
        draw_landmarks(image, results)
        
        # 2. Prediction logic
        keypoints = extract_keypoints(results)
        
        sequence.append(keypoints)
        sequence = sequence[-30:]
        
        if len(sequence) == 30:
            res = model.predict(np.expand_dims(sequence, axis=0))[0]
            print(actions[np.argmax(res)])
            
            
        #3. Viz logic
            if res[np.argmax(res)] > threshold: 
                if len(sentence) > 0: 
                    if actions[np.argmax(res)] != sentence[-1]:
                        sentence.append(actions[np.argmax(res)])
                else:
                    sentence.append(actions[np.argmax(res)])

            if len(sentence) > 5: 
                sentence = sentence[-5:]

            # Viz probabilities
            image = prob_viz(res, actions, image, colors)
            
        cv2.rectangle(image, (0,0), (640, 40), (245, 117, 16), -1)
        cv2.putText(image, ' '.join(sentence), (3,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        # Show to screen
        cv2.imshow('OpenCV Feed', image)

        # Break gracefully
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()