import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread("Asset/heli.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges
edges = cv2.Canny(blur, 50, 150)

# Copy original image
result = image.copy()

# Apply Hough Line Transform
lines = cv2.HoughLinesP(
    edges,
    1,
    np.pi / 180,
    50,
    minLineLength=30,
    maxLineGap=10
)

print(lines)
print(lines.shape if lines is not None else "No lines detected")

# Draw detected lines
if lines is not None:

    for line in lines:

        x1, y1, x2, y2 = line

        cv2.line(
            result,
            (int(x1), int(y1)),
            (int(x2), int(y2)),
            (0, 0, 255),
            2
        )

# Display
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original")

plt.subplot(1, 3, 2)
plt.imshow(edges, cmap="gray")
plt.title("Canny Edges")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title("Hough Line Detection")

plt.show()