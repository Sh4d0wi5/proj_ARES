import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load grayscale image
image = cv2.imread("Assetcode ./heli.jpg", 0)

# Apply binary threshold
ret, threshold = cv2.threshold(
    image, 127, 255, cv2.THRESH_BINARY
)

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Apply closing
closing = cv2.morphologyEx(
    threshold,
    cv2.MORPH_CLOSE,
    kernel,
    iterations=1
)

# Display
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap="gray")
plt.title("Original")

plt.subplot(1, 3, 2)
plt.imshow(threshold, cmap="gray")
plt.title("Threshold")

plt.subplot(1, 3, 3)
plt.imshow(closing, cmap="gray")
plt.title("Closing")

plt.show()