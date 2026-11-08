import cv2
import numpy as np

# 1. Read image
#path = r"D:\Codex\Proj_ARES\Asset\road.jpg"
image = cv2.imread("Asset/road.jpg")

if image is None:
    print("Image not found!")
    exit()

print("Original image shape:", image.shape)

# 2. Resize image
resized = cv2.resize(image, (640, 360))

# 3. Convert BGR to grayscale
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# 4. Apply Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 5. Apply Canny Edge Detection
edges = cv2.Canny(blur, 60, 20)

# 6. Display results
cv2.imshow("Original Image", resized)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Gaussian Blur", blur)
cv2.imshow("Canny Edge Detection", edges)

# 7. Wait for keyboard input
cv2.waitKey(0)

# 8. Close all windows
cv2.destroyAllWindows()