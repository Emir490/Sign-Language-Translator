import os
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import TensorBoard, EarlyStopping
from keras.optimizers import SGD
from ..utils.index import actions

# Load the train, validation, and test data
X_train = np.load('X_train.npy')
X_val = np.load('X_val.npy')  # Load the validation data
X_test = np.load('X_test.npy')
y_train = np.load('y_train.npy')
y_val = np.load('y_val.npy')  # Load the validation labels
y_test = np.load('y_test.npy')

log_dir = os.path.join('Logs')
tb_callback = TensorBoard(log_dir=log_dir)

print(X_train.shape)

model = Sequential()
model.add(LSTM(64, return_sequences=True, input_shape=(30, 1662)))
model.add(LSTM(128, return_sequences=True))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(actions.shape[0], activation='softmax'))

opt = SGD(learning_rate=0.01)
model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['categorical_accuracy'])

# Configure the early stopping callback
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Include the validation data and early stopping in the fit() method
model.fit(X_train, y_train, epochs=150, callbacks=[tb_callback, early_stopping], validation_data=(X_val, y_val))

model.summary()

res = model.predict(X_test)
print(actions[np.argmax(res[4])])
print(actions[np.argmax(y_test[4])])

model.save('model')