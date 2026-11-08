
import cv2
import matplotlib.pyplot as plt
import math

# Load original image
#path = r"D:\Codex\Proj_ARES\Asset\road.jpg"
image = cv2.imread("Asset/road.jpg")

if image is None:
    print("Image not found!")
    exit()

print("Original Image:", image.shape)

# Get image dimensions
image_height, image_width = image.shape[:2]

# Bounding box using complete image dimensions
x = 0
y = 0
w = image_width
h = image_height

# Calculate bounding box centre
cx = x + w // 2
cy = y + h // 2

# Calculate image centre
ix = image_width // 2
iy = image_height // 2

# Calculate displacement
dx = cx - ix
dy = cy - iy

# Calculate Euclidean distance
distance = math.sqrt(dx**2 + dy**2)

# Draw bounding box
cv2.rectangle(image, (x, y), (x+w-1, y+h-1), (0, 255, 0), 3)

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

# Display image
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Bounding Box Without Contours")
plt.axis("off")
plt.show()
