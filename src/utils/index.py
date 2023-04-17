import cv2
import numpy as np
import mediapipe as mp
import random

mp_holistic = mp.solutions.holistic # Holistic model
mp_drawing = mp.solutions.drawing_utils # Drawing utilities

# Actions that we try to detect
actions = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # COLOR CONVERSION BGR 2 RGB
    image.flags.writeable = False                  # Image is no longer writeable
    results = model.process(image)                 # Make prediction
    image.flags.writeable = True                   # Image is now writeable 
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # COLOR COVERSION RGB 2 BGR
    return image, results

def draw_landmarks(image, results):
    # Draw face connections
    mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION, 
                             mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1), 
                             mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)
                             ) 
    # Draw pose connections
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                             mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                             ) 
    # Draw left hand connections
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                             mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                             ) 
    # Draw right hand connections  
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                             mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                             ) 
    
def extract_keypoints(results):
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33*4)
    face = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(468*3)
    lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
    rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
    return np.concatenate([pose, face, lh, rh])

colors = [
    (245, 117, 16), (117, 245, 16), (16, 117, 245), # first 3 colors
    (245, 16, 117), (117, 16, 245), (16, 245, 117), # next 3 colors
    (245, 245, 16), (16, 245, 245), (245, 16, 245), # next 3 colors
    (245, 117, 245), (117, 245, 245), (245, 245, 117), # next 3 colors
    (117, 16, 16), (16, 117, 16), (16, 16, 117), # next 3 colors
    (117, 117, 16), (16, 117, 117), (117, 16, 117), # next 3 colors
    (117, 245, 16), (16, 245, 117), (245, 16, 117), # next 3 colors
    (117, 16, 245), (16, 117, 245), (245, 117, 16) # last 3 colors
]


def augment_keypoints(keypoints, noise_scale=0.01, scale_range=(0.9, 1.1), rotation_range=(-15, 15), translation_range=(-10, 10)):
    num_keypoints = keypoints.shape[0] // 2

    # Add Gaussian noise
    keypoints[:num_keypoints*2] += np.random.normal(0, noise_scale, num_keypoints*2)

    # Apply scaling
    scale = np.random.uniform(scale_range[0], scale_range[1])
    keypoints[:num_keypoints*2] *= scale

    # Apply rotation
    angle = np.radians(np.random.uniform(rotation_range[0], rotation_range[1]))
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])

    for i in range(0, num_keypoints*2, 2):
        keypoints[i:i+2] = np.dot(keypoints[i:i+2], rotation_matrix)

    # Apply translation
    translation_x = np.random.uniform(translation_range[0], translation_range[1])
    translation_y = np.random.uniform(translation_range[0], translation_range[1])
    keypoints[0:num_keypoints*2:2] += translation_x
    keypoints[1:num_keypoints*2:2] += translation_y

    return keypoints


# Augment a single sequence of keypoints
def augment_sequence(X, y, num_augmentations=5):
    X_augmented = []
    y_augmented = []

    for i in range(X.shape[0]):
        sequence = X[i]
        label = y[i]

        # Add the original sequence
        X_augmented.append(sequence)
        y_augmented.append(label)

        # Create augmented sequences
        for _ in range(num_augmentations):
            augmented_sequence = []
            for frame in sequence:
                augmented_keypoints = augment_keypoints(frame)
                augmented_sequence.append(augmented_keypoints)

            X_augmented.append(np.array(augmented_sequence))
            y_augmented.append(label)

    X_augmented = np.array(X_augmented)
    y_augmented = np.array(y_augmented)

    return X_augmented, y_augmented
