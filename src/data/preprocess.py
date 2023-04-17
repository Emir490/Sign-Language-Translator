import os
import time
import numpy as np
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from ..utils.index import actions, augment_sequence

DATA_PATH = os.path.join('data')

# TSixty videos worth of data
no_sequences = 60

# Videos are going to be 30 frames in length
sequence_length = 30

label_map = {label: num for num, label in enumerate(actions)}

start_time = time.time()

sequences, labels = [], []
for action in actions:
    for sequence in np.array(os.listdir(os.path.join(DATA_PATH, action))).astype(int):
        window = []
        for frame_num in range(sequence_length):
            res = np.load(os.path.join(DATA_PATH, action, str(sequence), "{}.npy".format(frame_num)))
            window.append(res)
        sequences.append(window)
        labels.append(label_map[action])

end_time = time.time()

time_taken = end_time - start_time
minutes, seconds = divmod(time_taken, 60)

print(f"Time taken: {int(minutes)} minutes and {int(seconds)} seconds")

X = np.array(sequences)
y = to_categorical(labels).astype(int)

X_augmented, y_augmented = augment_sequence(X, y)
    
X_augmented = np.array(X_augmented)
y_augmented = np.array(y_augmented)

X_train, X_test, y_train, y_test = train_test_split(X_augmented, y_augmented, test_size=0.05)