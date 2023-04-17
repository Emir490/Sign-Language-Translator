import os
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import TensorBoard, EarlyStopping
import sys

current = os.path.dirname(os.path.realpath(__file__)) # getting the name of the directory where this file is present.
parent = os.path.dirname(current) # Getting the parent directory name where the current directory is present.
sys.path.append(parent) # adding the parent directory to the sys.path.

from data.preprocess import actions, X_train, y_train, X_test, y_test

log_dir = os.path.join('Logs')
tb_callback = TensorBoard(log_dir=log_dir)
print(len(actions))

model = Sequential([
    LSTM(64, return_sequences=True, activation='relu',input_shape=(30, 1662)),
    LSTM(128, return_sequences=True, activation='relu'),
    LSTM(64, return_sequences=False, activation='relu'),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(actions.shape[0], activation='softmax')
])

early_stopping = EarlyStopping(monitor='categorical_accuracy', patience=50, restore_best_weights=True)
model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
model.fit(X_train, y_train, epochs=2000, callbacks=[tb_callback, early_stopping], validation_split=0.1)

model.summary()

res = model.predict(X_test)
print(actions[np.argmax(res[4])])
print(actions[np.argmax(y_test[4])])

model.save('model')