
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load helipad image
#path = r"D:\Codex\Proj_ARES\Asset\road.jpg"
image = cv2.imread("Asset/heli.jpg")

if image is None:
    print("Image not found!")
    exit()

print("Image Shape:", image.shape)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Otsu thresholding
_, binary = cv2.threshold(
    blur, 0, 255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

############################# 7.6 Adding Thresholding to Remove Noise #############################

# Find contours
contours, hierarchy = cv2.findContours(
    binary,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

print("Total contours detected:", len(contours))

# Create copy for drawing
output = image.copy()

# Draw all detected contours
cv2.drawContours(output, contours, -1, (0, 255, 0), 2)

# Display result
plt.figure(figsize=(10, 6))
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title("Detected Helipad Contours")
plt.axis("off")
plt.show()

########################################################################################################

# Display results
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Helipad Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(binary, cmap="gray")
plt.title("Thresholded Image")
plt.axis("off")

plt.show()
