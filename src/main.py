import pickle
import matplotlib.pyplot as plt

# Load the pickle file
with open('data/raw/PALABRAS.pickle', 'rb') as f:
    data = pickle.load(f)
    
# Extract the image and label data
images = data[0]
labels = data[1]

# Display the first 5 images with their labels
for i in range(5):
    plt.imshow(images[i])
    plt.title(f'Label: {labels[i]}')
    plt.show()