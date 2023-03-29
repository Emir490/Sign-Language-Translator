import pickle
import matplotlib.pyplot as plt
from PIL import Image

# Load the pickle file
with open('data/raw/PALABRAS.pickle', 'rb') as f:
    data = pickle.load(f)   
    
print(data)
    
# Extract the image and label data
# images = data[0]
# labels = data[1]

# Display the first 5 images with their labels
# for i in range(5):
#     print(images[i])
#     plt.title(f'Label: {labels[i]}')
#     plt.show()