import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create a black image
image = np.zeros((400, 600), dtype=np.uint8)

# Draw separate white objects
cv2.rectangle(image, (50, 50), (150, 150), 255, -1)
cv2.circle(image, (300, 100), 50, 255, -1)
cv2.rectangle(image, (400, 200), (550, 350), 255, -1)

plt.imshow(image, cmap='gray')
plt.title("Binary Image")
plt.axis("off")
plt.show()

# STEP 2: Connected Components Analysis
#num_labels, labels = cv2.connectedComponents(image)
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(image)

print("Number of labels:", num_labels)

# STEP 3: Normalize labels for visualization
label_image = (labels * 80).astype(np.uint8)

plt.imshow(label_image, cmap='nipy_spectral')
plt.title("Connected Components - Labels")
plt.axis("off")
plt.show()

print("Unique labels:", np.unique(labels))

print("Label at object 1:", labels[100, 100])
print("Label at object 2:", labels[100, 300])
print("Label at object 3:", labels[250, 450])

# STEP 4: Extract Object Properties

for i in range(1, num_labels):

    x = stats[i, cv2.CC_STAT_LEFT]
    y = stats[i, cv2.CC_STAT_TOP]

    w = stats[i, cv2.CC_STAT_WIDTH]
    h = stats[i, cv2.CC_STAT_HEIGHT]

    area = stats[i, cv2.CC_STAT_AREA]

    cx, cy = centroids[i]

    print(f"\nObject {i}")
    print("X:", x)
    print("Y:", y)
    print("Width:", w)
    print("Height:", h)
    print("Area:", area)
    print("Centroid:", cx, cy)

# STEP 5: Draw Bounding Boxes and Centroids

output = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

for i in range(1, num_labels):

    x = stats[i, cv2.CC_STAT_LEFT]
    y = stats[i, cv2.CC_STAT_TOP]

    w = stats[i, cv2.CC_STAT_WIDTH]
    h = stats[i, cv2.CC_STAT_HEIGHT]

    cx, cy = centroids[i]

    # Draw bounding box
    cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Draw centroid
    cv2.circle(output, (int(cx), int(cy)), 5, (0, 0, 255), -1)

    # Add object ID
    cv2.putText(output, f"Object {i}",
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (255, 0, 0), 2)

plt.figure(figsize=(10, 6))
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title("Connected Components - Object Detection")
plt.axis("off")
plt.show()

# STEP 6: Filter objects based on area

output = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

min_area = 8000

for i in range(1, num_labels):

    area = stats[i, cv2.CC_STAT_AREA]

    if area > min_area:

        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]

        cx, cy = centroids[i]

        cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.circle(output, (int(cx), int(cy)), 5, (0, 0, 255), -1)

        print(f"Object {i} detected | Area: {area}")

plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title("Area-Based Object Filtering")
plt.axis("off")
plt.show()