import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the image
image = cv2.imread("Asset/heli.jpg")

if image is None:
    print("Error: Image not found. Check the file path.")
    exit()

# Step 2: Convert BGR to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 4: Otsu Thresholding
_, otsu = cv2.threshold(
    blur,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# Step 5: Adaptive Thresholding
adaptive = cv2.adaptiveThreshold(
    blur,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    31,
    5
)

# Step 6: Adaptive Thresholding Inverted
adaptive_inv = cv2.adaptiveThreshold(
    blur,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    31,
    5
)

# Step 7: Display all results
images = [
    gray,
    otsu,
    adaptive,
    adaptive_inv
]

titles = [
    "Original Grayscale",
    "Otsu Threshold",
    "Adaptive Threshold",
    "Adaptive Inverted Threshold"
]

plt.figure(figsize=(14, 9))

for i in range(len(images)):
    plt.subplot(2, 2, i + 1)

    plt.imshow(images[i], cmap="gray")

    plt.title(titles[i])

    plt.axis("off")

plt.tight_layout()
plt.show()