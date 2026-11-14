import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read grayscale image
image = cv2.imread("Asset/road.jpg", cv2.IMREAD_GRAYSCALE)

# Check image
if image is None:
    print("Image not found!")
    exit()

# Apply Global Thresholding
threshold_value = 127

ret, threshold = cv2.threshold(
    image,
    threshold_value,
    255,
    cv2.THRESH_BINARY
)

#STEP 2 :  Adaptive Mean Thresholding

adaptive_mean = cv2.adaptiveThreshold(
    image,   #Input grayscale image
    255,    #Maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types
    cv2.ADAPTIVE_THRESH_MEAN_C,  #Calculates local mean
    cv2.THRESH_BINARY,  #Binary output
    11,     #Block size (11 × 11 neighbourhood)
    2   #Constant subtracted from local mean
)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(adaptive_mean, cmap="gray")
plt.title("Adaptive Mean Thresholding")
plt.axis("off")

plt.show()

# Display images
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Grayscale")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(threshold, cmap="gray")
plt.title("Global Thresholding")
plt.axis("off")

plt.show()

#STEP 3: Adaptive Gaussian Thresholding

# Adaptive Gaussian Thresholding

adaptive_gaussian = cv2.adaptiveThreshold(
    image,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

# Display comparison

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(adaptive_mean, cmap="gray")
plt.title("Adaptive Mean")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(adaptive_gaussian, cmap="gray")
plt.title("Adaptive Gaussian")
plt.axis("off")

plt.show()

#step 4: # Compare different block sizes

block_3 = cv2.adaptiveThreshold(
    image, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 3, 2
)

block_11 = cv2.adaptiveThreshold(
    image, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 11, 2
)

block_21 = cv2.adaptiveThreshold(
    image, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 21, 2
)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(block_3, cmap="gray")
plt.title("Block Size 3")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(block_11, cmap="gray")
plt.title("Block Size 11")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(block_21, cmap="gray")
plt.title("Block Size 21")
plt.axis("off")

plt.show()

#step 5: Compare different C values

c_2 = cv2.adaptiveThreshold(
    image, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11, 2
)

c_5 = cv2.adaptiveThreshold(
    image, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11, 5
)

c_10 = cv2.adaptiveThreshold(
    image, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11, 10
)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(c_2, cmap="gray")
plt.title("C = 2")

plt.subplot(1, 3, 2)
plt.imshow(c_5, cmap="gray")
plt.title("C = 5")

plt.subplot(1, 3, 3)
plt.imshow(c_10, cmap="gray")
plt.title("C = 10")

plt.show()