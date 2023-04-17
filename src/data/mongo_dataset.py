import os
import json
import numpy as np
from ..utils.index import actions

DATA_PATH = os.path.join("ABC")

with open('JSON/actions.json', 'r') as f:
    action_data = []
    for line in f:
        action_data.append(json.loads(line))

for action in actions:
    print(action)
    for sequence in np.array(os.listdir(os.path.join(DATA_PATH, action))).astype(int) + 30:
        if sequence >= 30:
            action_keypoints = [item for item in action_data if item["action"] == action]
            for item in action_keypoints:
                landmarks = item["keypoints"]
                for i, frame in enumerate(landmarks):
                    pose = frame["pose"]
                    face = frame["face"]
                    rightHand = frame["rightHand"]
                    leftHand = frame["leftHand"]
                    keypoints = np.concatenate([pose, face, rightHand, leftHand])
                    npy_path = os.path.join(DATA_PATH, action, str(sequence), str(i))
                    if not os.path.exists(os.path.dirname(npy_path)):
                        os.makedirs(os.path.dirname(npy_path))
                    np.save(npy_path, keypoints)
                
                
                
                