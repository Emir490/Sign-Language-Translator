import os
import time
import json
import numpy as np
from ..utils.index import actions

DATA_PATH = "data"

start_time = time.time()

# Loop over the actions and sequences to save the keypoints to numpy files
for action in actions:
    print(action)
    videos = 30 if action == "LL" or action == "RR" else 60
    with open(os.path.join('merged', f"{action}.json"), 'r') as f:
        action_sequences = json.load(f)
    for i, sequence in enumerate(action_sequences):
        if action == sequence["action"]:
            landmarks = sequence["landmarks"]
            for j, frame in enumerate(landmarks):
                if j < 30:
                    pose = frame["pose"]
                    face = frame["face"]
                    rightHand = frame["rightHand"]
                    leftHand = frame["leftHand"]
                    keypoints = np.concatenate([pose, face, rightHand, leftHand])
                    npy_path = os.path.join(DATA_PATH, action, str(i + videos), str(j))
                    if not os.path.exists(os.path.dirname(npy_path)):
                        os.makedirs(os.path.dirname(npy_path))
                    np.save(npy_path, keypoints)
                    
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {int(elapsed_time // 60)}m {int(elapsed_time % 60)}s")