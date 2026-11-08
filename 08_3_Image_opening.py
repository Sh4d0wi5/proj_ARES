
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read image
image = cv2.imread("Asset/heli.jpg")

if image is None:
    print("Image not found!")
    exit()

# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Adaptive Inverted Threshold
adaptive_inv = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    31,
    5
)

# Step 4: Create kernel
kernel = np.ones((3, 3), np.uint8)

# Step 5: Apply Opening
opening = cv2.morphologyEx(
    adaptive_inv,
    cv2.MORPH_OPEN,
    kernel,
    iterations=1
)

# Step 6: Display results
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.imshow(adaptive_inv, cmap="gray")
plt.title("Before Opening")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(opening, cmap="gray")
plt.title("After Opening")
plt.axis("off")

plt.tight_layout()
plt.show()
