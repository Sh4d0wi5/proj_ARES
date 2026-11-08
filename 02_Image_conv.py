import cv2
import numpy as np

# 1. Read image
#path = r"D:\Codex\Proj_ARES\Asset\road.jpg"
image = cv2.imread("Asset/road.jpg")

if image is None:
    print("Image loading failed!")
    exit()

print("Image loaded successfully!")

# 2. Inspect image properties
print("Original shape:", image.shape)
print("Height:", image.shape[0])
print("Width:", image.shape[1])
print("Channels:", image.shape[2])
print("Data type:", image.dtype)

# 3. Resize image
resized = cv2.resize(image, (640, 360))

# 4. Convert to grayscale
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# 5. Crop Region of Interest
cropped = gray[50:250, 100:400]

# 6. Display images
cv2.imshow("Original Image", image)
cv2.imshow("Resized Image", resized)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Cropped Image", cropped)

# 7. Wait for key press
cv2.waitKey(0)

# 8. Close windows
cv2.destroyAllWindows()

########################## Diagnostic Script for Image Loading ##########################

'''import cv2
import os

path = r"D:\Codex\Proj_ARES\road.jpg"

print("1. Python working directory:", os.getcwd())
print("2. File exists:", os.path.exists(path))
print("3. File size:", os.path.getsize(path) if os.path.exists(path) else "File missing")

# Read image
image = cv2.imread(path)

print("4. OpenCV image:", image)

if image is None:
    print("ERROR: OpenCV failed to read the image.")
else:
    print("SUCCESS: Image loaded!")
    print("Image shape:", image.shape)

    cv2.imshow("Road Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''
