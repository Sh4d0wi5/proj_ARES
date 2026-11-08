import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

path = r"D:\Codex\Proj_ARES\Asset\heli.jpg"
image = cv2.imread(path)

if image is None:
    print("Image not found!")
    exit()

print("Original image:", image.shape)

# Create a black image
#image = np.zeros((400, 500, 3), dtype=np.uint8)

# Draw a white rectangle
#cv2.rectangle(image, (100, 100), (300, 250), (255, 255, 255), -1)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Otsu thresholding
_, binary = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# Display threshold image
plt.imshow(binary, cmap="gray")
plt.title("Binary Threshold Image")
plt.axis("off")
plt.show()

# Find contours
contours, hierarchy = cv2.findContours(
    gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

# Get the first contour
contour = contours[0]

# Calculate bounding box
x, y, w, h = cv2.boundingRect(contour)

# Draw bounding box
cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 3)

# Print coordinates
print("X:", x)
print("Y:", y)
print("Width:", w)
print("Height:", h)

# Display image
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Bounding Box")
plt.axis("off")
plt.show()

################################# Image Centre Calculation #################################
# Calculate centre point
cx = x + w // 2
cy = y + h // 2

print("Centre X:", cx)
print("Centre Y:", cy)

# Draw centre point
cv2.circle(image, (cx, cy), 5, (0, 0, 255), -1)


# Calculate image centre
image_height, image_width = image.shape[:2]

ix = image_width // 2
iy = image_height // 2

# Calculate object displacement
dx = cx - ix
dy = cy - iy

print("Image Centre:", ix, iy)
print("Object Centre:", cx, cy)
print("X Difference:", dx)
print("Y Difference:", dy)

#################################### Ecludian Distance Calculation ####################################

# Calculate Euclidean distance
distance = math.sqrt(dx**2 + dy**2)

print("Distance from Image Centre:", distance)