import cv2
import numpy as np

# 1. Read image
#path = r"D:\Codex\Proj_ARES\Asset\road.jpg"
image = cv2.imread("Asset/road.jpg")

if image is None:
    print("Image not found!")
    exit()

print("Image loaded successfully!")

# 2. Resize image
resized = cv2.resize(image, (640, 360))

# 3. Convert to grayscale
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# 4. Apply Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 5. Apply Canny Edge Detection
edges = cv2.Canny(blur, 100, 200)

# 6. Find contours
contours, hierarchy = cv2.findContours(
    edges,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

print("Total contours detected:", len(contours))

# 7. Draw contours
contour_image = resized.copy()

cv2.drawContours(
    contour_image,
    contours,
    -1,
    (0, 255, 0),
    1
)

# 8. Calculate contour areas
for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    print("Contour", i + 1, "Area:", area)

# 9. Display results
cv2.imshow("Original Image", resized)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Canny Edges", edges)
cv2.imshow("Detected Contours", contour_image)

# 10. Wait and close
cv2.waitKey(0)
cv2.destroyAllWindows()