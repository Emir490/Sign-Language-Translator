import numpy as np
from sklearn.metrics import multilabel_confusion_matrix, accuracy_score
from keras.models import load_model, Sequential
import sys
import os

current = os.path.dirname(os.path.realpath(__file__)) # getting the name of the directory where this file is present.
parent = os.path.dirname(current) # Getting the parent directory name where the current directory is present.
sys.path.append(parent) # adding the parent directory to the sys.path.

from data.preprocess import X_test, y_test

model : Sequential = load_model('model')

yhat = model.predict(X_test)

ytrue = np.argmax(y_test, axis=1).tolist()
yhat = np.argmax(yhat, axis=1).tolist()

print(multilabel_confusion_matrix(ytrue, yhat))

print(accuracy_score(ytrue, yhat))