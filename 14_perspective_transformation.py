import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread("Asset/heli.jpg")

# Get image dimensions
height, width = image.shape[:2]

# Define four source points
src_points = np.float32([
    [126, 118],   # Top-left
    [548, 115],   # Top-right
    [550, 328],   # Bottom-right
    [24, 327]     # Bottom-left
])

# Define destination points
output_width = 600
output_height = 300

dst_points = np.float32([
    [0, 0],
    [output_width - 1, 0],
    [output_width - 1, output_height - 1],
    [0, output_height - 1]
])

# Calculate perspective matrix
matrix = cv2.getPerspectiveTransform(
    src_points,
    dst_points
)

# Apply perspective transformation
warped = cv2.warpPerspective(
    image,
    matrix,
    (output_width, output_height)
)

# Display results
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(warped, cv2.COLOR_BGR2RGB))
plt.title("Bird's Eye View")

plt.show()