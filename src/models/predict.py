import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from keras.models import load_model, Sequential
from sklearn.metrics import multilabel_confusion_matrix, accuracy_score, precision_recall_fscore_support, confusion_matrix

X_test = np.load('X_test.npy')
y_test = np.load('y_test.npy')

model : Sequential = load_model('model')

yhat = model.predict(X_test)

ytrue = np.argmax(y_test, axis=1).tolist()
yhat = np.argmax(yhat, axis=1).tolist()

# Compute multilabel confusion matrix
print("Multilabel Confusion Matrix:")
print(multilabel_confusion_matrix(ytrue, yhat))

# Compute accuracy
print("Accuracy:", accuracy_score(ytrue, yhat))

# Compute precision, recall, F1-score, and support
precision, recall, f1_score, _ = precision_recall_fscore_support(ytrue, yhat, average='weighted')

print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1_score)

cm = confusion_matrix(ytrue, yhat)

plt.figure(figsize=(10, 10))
sns.heatmap(cm, annot=True, cmap='Blues', fmt='d', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix Heatmap')
plt.show()

_, _, f1_scores, _ = precision_recall_fscore_support(ytrue, yhat)
accuracies = cm.diagonal() / cm.sum(axis=1)

plt.figure(figsize=(10, 5))
plt.bar(range(len(accuracies)), accuracies)
plt.xlabel('Class')
plt.ylabel('Accuracy')
plt.title('Class-wise Accuracies')
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(range(len(f1_scores)), f1_scores)
plt.xlabel('Class')
plt.ylabel('F1-score')
plt.title('Class-wise F1-scores')
plt.show()