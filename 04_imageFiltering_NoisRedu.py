import cv2
import numpy as np

# 1. Read image
#path = r"D:\Codex\Proj_ARES\Asset\road.jpg"
image = cv2.imread("Asset/road.jpg")

if image is None:
    print("Image not found!")
    exit()

print("Original image:", image.shape)

# 2. Resize image
resized = cv2.resize(image, (640, 360))

# 3. Apply Gaussian Blur
gaussian = cv2.GaussianBlur(resized, (5, 5), 0)

# 4. Apply Median Blur
median = cv2.medianBlur(resized, 5)

# 5. Apply Bilateral Filter
bilateral = cv2.bilateralFilter(resized, 9, 75, 75)

# 6. Display images
cv2.imshow("Original Image", resized)
cv2.imshow("Gaussian Blur", gaussian)
cv2.imshow("Median Blur", median)
cv2.imshow("Bilateral Filter", bilateral)

# 7. Wait for key
cv2.waitKey(0)

# 8. Close windows
cv2.destroyAllWindows()