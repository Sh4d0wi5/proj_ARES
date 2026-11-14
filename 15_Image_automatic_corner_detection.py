import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread("Asset/heli.jpg")

if image is None:
    raise FileNotFoundError("Image not found")

original = image.copy()

# Step 1: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 2: Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 3: Edge Detection
edges = cv2.Canny(blur, 50, 150)

# Step 4: Find contours
contours, hierarchy = cv2.findContours(
    edges,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Step 5: Detect four-corner polygons
for contour in contours:

    perimeter = cv2.arcLength(contour, True)

    approx = cv2.approxPolyDP(
        contour,
        0.02 * perimeter,
        True
    )

    # Check whether polygon has four corners
    if len(approx) == 4:

        cv2.drawContours(
            original,
            [approx],
            -1,
            (0, 255, 0),
            3
        )

        for point in approx:
            x, y = point[0]

            cv2.circle(
                original,
                (x, y),
                7,
                (0, 0, 255),
                -1
            )

# Display results
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
plt.title("Automatic Corner Detection")

plt.show()