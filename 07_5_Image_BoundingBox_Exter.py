
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read image
image = cv2.imread("Asset/heli.jpg")

if image is None:
    print("Image not found!")
    exit()

# Step 2: Select the helipad region manually
roi = cv2.selectROI(
    "Select Helipad Region",
    image,
    showCrosshair=True,
    fromCenter=False
)

x, y, w, h = roi

if w == 0 or h == 0:
    print("No ROI selected!")
    exit()

cropped = image[y:y+h, x:x+w]

# Step 3: Convert cropped image to grayscale
gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

# Step 4: Apply Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 5: Otsu Thresholding
_, threshold = cv2.threshold(
    blur,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# Step 6: Morphological operations
kernel = np.ones((3, 3), np.uint8)

cleaned = cv2.morphologyEx(
    threshold,
    cv2.MORPH_OPEN,
    kernel
)

cleaned = cv2.morphologyEx(
    cleaned,
    cv2.MORPH_CLOSE,
    kernel
)

# Step 7: Find contours
contours, hierarchy = cv2.findContours(
    cleaned,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Step 8: Draw bounding boxes
output = cropped.copy()

for contour in contours:

    area = cv2.contourArea(contour)

    if area > 80:

        x1, y1, w1, h1 = cv2.boundingRect(contour)

        cv2.rectangle(
            output,
            (x1, y1),
            (x1 + w1, y1 + h1),
            (0, 255, 0),
            2
        )

# Step 9: Display results
images = [
    cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB),
    cleaned,
    cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
]

titles = [
    "Cropped Helipad",
    "Threshold + Morphology",
    "Bounding Box Detection"
]

plt.figure(figsize=(15, 6))

for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], cmap="gray" if i == 1 else None)
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()

cv2.destroyAllWindows()
