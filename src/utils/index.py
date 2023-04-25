import numpy as np

# Actions that we try to detect
actions = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'LL', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'RR', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

def augment_keypoints(keypoints, noise_scale=0.01, scale_range=(0.9, 1.1), rotation_range=(-15, 15), translation_range=(-10, 10)):
    num_keypoints = keypoints.shape[0] // 2

    # Add Gaussian noise
    keypoints[:num_keypoints*2] += np.random.normal(0, noise_scale, num_keypoints*2)

    # Apply scaling
    scale = np.random.uniform(scale_range[0], scale_range[1])
    keypoints[:num_keypoints*2] *= scale

    # Apply rotation
    angle = np.radians(np.random.uniform(rotation_range[0], rotation_range[1]))
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])

    for i in range(0, num_keypoints*2, 2):
        keypoints[i:i+2] = np.dot(keypoints[i:i+2], rotation_matrix)

    # Apply translation
    translation_x = np.random.uniform(translation_range[0], translation_range[1])
    translation_y = np.random.uniform(translation_range[0], translation_range[1])
    keypoints[0:num_keypoints*2:2] += translation_x
    keypoints[1:num_keypoints*2:2] += translation_y

    return keypoints


# Augment a single sequence of keypoints
def augment_sequence(X, y, num_augmentations=2):
    X_augmented = []
    y_augmented = []

    for i in range(X.shape[0]):
        sequence = X[i]
        label = y[i]

        # Add the original sequence
        X_augmented.append(sequence)
        y_augmented.append(label)

        # Create augmented sequences
        for _ in range(num_augmentations):
            augmented_sequence = []
            for frame in sequence:
                augmented_keypoints = augment_keypoints(frame)
                augmented_sequence.append(augmented_keypoints)

            X_augmented.append(np.array(augmented_sequence))
            y_augmented.append(label)

    X_augmented = np.array(X_augmented)
    y_augmented = np.array(y_augmented)

    return X_augmented, y_augmented
