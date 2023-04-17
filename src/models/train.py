import os
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import TensorBoard, EarlyStopping
from ..data.preprocess import actions, X_train, y_train, X_test, y_test

log_dir = os.path.join('Logs')
tb_callback = TensorBoard(log_dir=log_dir)

print(X_train.shape)

model = Sequential()
model.add(LSTM(64, return_sequences=True, input_shape=(30,1662)))
model.add(LSTM(128, return_sequences=True))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(actions.shape[0], activation='softmax'))

early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
model.compile(optimizer='Adam', loss="categorical_crossentropy", metrics=['categorical_accuracy'])
model.fit(X_train, y_train, epochs=2000, callbacks=[tb_callback, early_stopping], validation_split=0.1)

model.summary()

res = model.predict(X_test)
print(actions[np.argmax(res[4])])
print(actions[np.argmax(y_test[4])])

model.save('model')