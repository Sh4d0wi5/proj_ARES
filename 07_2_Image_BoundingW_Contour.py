
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

# Load original image
#path = r"D:\Codex\Proj_ARES\Asset\road.jpg"
image = cv2.imread("Asset/road.jpg")

if image is None:
    print("Image not found!")
    exit()

print("Original Image:", image.shape)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Otsu thresholding
_, binary = cv2.threshold(
    gray, 0, 255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# Find contours
contours, hierarchy = cv2.findContours(
    binary,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

print("Number of contours:", len(contours))

if len(contours) == 0:
    print("No contours detected!")
    exit()

# Find largest contour
contour = max(contours, key=cv2.contourArea)

# Calculate bounding box
x, y, w, h = cv2.boundingRect(contour)

# Calculate object centre
cx = x + w // 2
cy = y + h // 2

# Calculate image centre
image_height, image_width = image.shape[:2]

ix = image_width // 2
iy = image_height // 2

# Calculate displacement
dx = cx - ix
dy = cy - iy

# Calculate Euclidean distance
distance = math.sqrt(dx**2 + dy**2)

# Draw bounding box
cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 3)

# Draw centre point
cv2.circle(image, (cx, cy), 5, (0, 0, 255), -1)

# Print results
print("X:", x)
print("Y:", y)
print("Width:", w)
print("Height:", h)

print("Object Centre:", cx, cy)
print("Image Centre:", ix, iy)

print("X Difference:", dx)
print("Y Difference:", dy)

print("Distance from Image Centre:", distance)

# Display binary image
plt.figure()
plt.imshow(binary, cmap="gray")
plt.title("Binary Image")
plt.axis("off")

# Display bounding box
plt.figure()
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Bounding Box Using Contours")
plt.axis("off")
plt.show()
