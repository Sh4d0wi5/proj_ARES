
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create a sample image: 300 x 300 pixels
image = np.zeros((300, 500, 3), dtype=np.uint8)

# Draw colored shapes
image[50:70, 50:150] = [255, 255, 255]    # Red in BGR
image[50:300, 150:300] = [255, 255, 255]  # Green in BGR
image[150:250, 50:150] = [255, 0, 200]  # Blue in BGR
image[150:250, 150:250] = [255, 255, 255] # Yellow in BGR
image[100:200, 300:400] = [255, 255, 255] # Magenta in BGR

# Inspect image properties
print("Image shape:", image.shape)
print("Data type:", image.dtype)
print("Pixel value:", image[100, 100])

# Display using OpenCV
cv2.imshow("ARES - Image Basics", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
