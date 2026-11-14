import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread("Asset/heli.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
blur = cv2.GaussianBlur(gray, (9, 9), 2)

# Detect circles
circles = cv2.HoughCircles(
    blur,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=100,
    param1=100,
    param2=60,
    minRadius=50,
    maxRadius=180
)

# Copy original image
result = image.copy()

# Draw detected circles
if circles is not None:

    circles = np.uint16(np.around(circles))

    for circle in circles[0, :]:

        x, y, r = circle

        # Draw outer circle
        cv2.circle(
            result,
            (x, y),
            r,
            (0, 0, 255),
            2
        )

        # Draw centre point
        cv2.circle(
            result,
            (x, y),
            3,
            (0, 255, 0),
            -1
        )

    print("Number of circles detected:", len(circles[0]))

else:
    print("No circles detected")

# Display results
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")

plt.subplot(1, 3, 2)
plt.imshow(blur, cmap="gray")
plt.title("Gaussian Blur")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title("Hough Circle Detection")

plt.show()