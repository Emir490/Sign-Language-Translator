import os
import time
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.utils import to_categorical
from ..utils.index import actions
from multiprocessing import Pool

DATA_PATH = os.path.join('data')

# Three hundred videos worth of data
no_sequences = 300

# Videos are going to be 30 frames in length
sequence_length = 30

label_map = {label: num for num, label in enumerate(actions)}

def load_sequence(args):
    action, sequence = args
    window = []
    for frame_num in range(sequence_length):
        res = np.load(os.path.join(DATA_PATH, action, str(sequence), "{}.npy".format(frame_num)))
        window.append(res)
    return window, label_map[action]

def main():
    start_time = time.time()

    sequences, labels = [], []

    with Pool() as pool:
        for action in actions:
            print(action)
            sequence_nums = np.array(os.listdir(os.path.join(DATA_PATH, action))).astype(int)
            sequence_data = pool.map(load_sequence, [(action, seq) for seq in sequence_nums])
            seqs, labs = zip(*sequence_data)
            sequences.extend(seqs)
            labels.extend(labs)

    end_time = time.time()

    time_taken = end_time - start_time
    minutes, seconds = divmod(time_taken, 60)

    print(f"Time taken: {int(minutes)} minutes and {int(seconds)} seconds")

    X = np.array(sequences)

    # Normalize the input data
    scaler = StandardScaler()
    X_shape = X.shape
    X = scaler.fit_transform(X.reshape(-1, X_shape[-1])).reshape(X_shape)

    y = to_categorical(labels).astype(int)

    # X_augmented, y_augmented = augment_sequence(X, y)
        
    # X_augmented = np.array(X_augmented)
    # y_augmented = np.array(y_augmented)

   # First, split the dataset into train and temp (which will be later split into validation and test)
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2)  # 80% training, 20% temp

    # Now, split the temp set into validation and test sets
    validation_ratio = 0.5  # Use 50% of the temp set for validation and the remaining 50% for testing
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=validation_ratio)

    return X_train, X_val, X_test, y_train, y_val, y_test

if __name__ == '__main__':
    X_train, X_val, X_test, y_train, y_val, y_test = main()
    np.save('X_train.npy', X_train)
    np.save('X_test.npy', X_test)
    np.save('X_val.npy', X_val)
    np.save('y_val.npy', y_val)
    np.save('y_train.npy', y_train)
    np.save('y_test.npy', y_test)