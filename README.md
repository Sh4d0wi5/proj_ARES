# Project ARES

A step-by-step collection of **OpenCV image-processing lessons in Python**, building from basic pixel manipulation up to thresholding, contour detection, bounding boxes, and morphological operations. The later lessons work toward locating a target (a helipad) in an image and measuring how far it sits from the image centre, which is the kind of building block used in vision-guided navigation and landing.

Each numbered script is standalone and designed to be read and run in order.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Lesson Guide](#lesson-guide)
- [Sample Assets](#sample-assets)
- [Known Issues](#known-issues)
- [Roadmap](#roadmap)

---

## Features

- Image creation, loading, resizing, cropping, and colour-space conversion
- Image format verification and conversion (Pillow)
- Noise reduction with Gaussian, Median, and Bilateral filters
- Canny edge detection
- Contour detection, drawing, and area calculation
- Global (Otsu) and adaptive thresholding
- Bounding boxes, object centre, and Euclidean distance from the image centre
- Interactive region-of-interest selection with `cv2.selectROI`
- Morphological operations: erosion, dilation, opening, and closing

## Project Structure

```
proj_ARES/
├── Asset/
│   ├── road.jpg              # Sample road image (751 x 500)
│   ├── road.AVIF             # Original road image in AVIF format
│   ├── road_converted.jpg    # road image after format conversion
│   ├── heli.jpg              # Sample helipad image (408 x 612)
│   └── heli_converted.jpg    # helipad image after format conversion
├── 01_image_basics.py
├── 02_Image_conv.py
├── 03_Image_FormatCheck.py
├── 04_imageFiltering_NoisRedu.py
├── 05_Image_EdgeDetct.py
├── 06_image_countourDetct.py
├── 07_Image_BoundingBox.py
├── 07_1_Image_boundingWO_Contour.py
├── 07_2_Image_BoundingW_Contour.py
├── 07_3_Image_segmentation.py
├── 07_4_Image_Seg_Debug.py
├── 07_5_Image_BoundingBox_Exter.py
├── 08_Image_Morphological.py
├── 08_1_Image_dilation.py
├── 08_3_Image_opening.py
└── README.md
```

## Requirements

- Python 3.8+
- [opencv-python](https://pypi.org/project/opencv-python/)
- [numpy](https://pypi.org/project/numpy/)
- [matplotlib](https://pypi.org/project/matplotlib/)
- [Pillow](https://pypi.org/project/pillow/) (used in lesson 03)

A desktop environment is needed, since the scripts open GUI windows via `cv2.imshow` and `matplotlib`.

## Installation

```bash
# Clone the repository
git clone https://github.com/Sh4d0wi5/proj_ARES.git
cd proj_ARES

# (Recommended) create a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Install dependencies
pip install opencv-python numpy matplotlib pillow
```

## Usage

Run scripts **from the repository root**, because images are loaded using relative paths like `Asset/road.jpg`.

```bash
python 01_image_basics.py
python 05_Image_EdgeDetct.py
python 07_5_Image_BoundingBox_Exter.py
```

For the `cv2.imshow` windows, press any key to close them. Matplotlib windows close with the window's close button.

## Lesson Guide

| # | Script | Topic | Image used |
|---|--------|-------|------------|
| 01 | `01_image_basics.py` | Build a blank image with NumPy, draw coloured regions, inspect shape, dtype, and pixel values | Generated |
| 02 | `02_Image_conv.py` | Load, inspect, resize, convert to grayscale, crop a region of interest | `road.jpg` |
| 03 | `03_Image_FormatCheck.py` | Verify an image's real format with Pillow and convert it to JPEG (quality 95) | `road.jpg`, `heli.jpg` |
| 04 | `04_imageFiltering_NoisRedu.py` | Compare Gaussian, Median, and Bilateral filtering | `road.jpg` |
| 05 | `05_Image_EdgeDetct.py` | Grayscale, blur, then Canny edge detection | `road.jpg` |
| 06 | `06_image_countourDetct.py` | Canny edges, `findContours`, `drawContours`, and per-contour area | `road.jpg` |
| 07 | `07_Image_BoundingBox.py` | Bounding box, centre point, and Euclidean distance from the image centre | `heli.jpg` |
| 07.1 | `07_1_Image_boundingWO_Contour.py` | Baseline: a bounding box covering the full image, without contours | `road.jpg` |
| 07.2 | `07_2_Image_BoundingW_Contour.py` | Otsu threshold, largest contour, bounding box, centre, and distance | `road.jpg` |
| 07.3 | `07_3_Image_segmentation.py` | Blur, Otsu threshold, and contour overlay for the helipad | `heli.jpg` |
| 07.4 | `07_4_Image_Seg_Debug.py` | Side-by-side comparison of Otsu, adaptive, and inverted adaptive thresholds | `heli.jpg` |
| 07.5 | `07_5_Image_BoundingBox_Exter.py` | Interactive ROI selection, threshold, open/close cleanup, area-filtered bounding boxes | `heli.jpg` |
| 08 | `08_Image_Morphological.py` | Erosion on an adaptive-threshold mask | `heli.jpg` |
| 08.1 | `08_1_Image_dilation.py` | Dilation on an adaptive-threshold mask | `heli.jpg` |
| 08.3 | `08_3_Image_opening.py` | Opening (erosion then dilation) to remove small noise | `heli.jpg` |

### Core concepts covered

- **Distance from centre:** the offset `(dx, dy)` between the detected object's centre and the image centre, and the Euclidean distance `sqrt(dx² + dy²)`. This is the core measurement in lessons 07 to 07.2.
- **Thresholding:** Otsu picks a global threshold automatically; adaptive thresholding computes one per neighbourhood, which handles uneven lighting better.
- **Morphology:** erosion shrinks white regions, dilation grows them, and opening removes small specks while preserving larger shapes.

## Sample Assets

The `Asset/` folder holds the images the lessons run on. `heli.jpg` is the helipad image used from lesson 07.3 onward; `road.jpg` is used in the earlier lessons. The `*_converted.jpg` files are outputs of the conversion step in lesson 03, and `road.AVIF` is the original-format source.

## Known Issues

These are worth fixing before relying on the scripts:

- **`03_Image_FormatCheck.py`** will fail as written: it uses `cv2` without importing it, references an undefined `path` variable, and the conversion section uses a hardcoded Windows path (`D:\Codex\Proj_ARES\...`).
- **`07_Image_BoundingBox.py`** also uses a hardcoded Windows path. It additionally passes the grayscale image (not the thresholded `binary` image) to `findContours` and takes `contours[0]` rather than the largest contour, so the box it draws may not be the helipad. Lesson 07.2 shows the more robust approach.
- **`05_Image_EdgeDetct.py`** calls `cv2.Canny(blur, 60, 20)`, with the lower threshold above the upper. OpenCV swaps them internally, but the conventional order is `(low, high)`, e.g. `(20, 60)`.
- **`01_image_basics.py`**: the comments label the colours (Red, Green, Yellow, and so on) but most regions are set to white, so the labels don't match the output.
- Matplotlib and OpenCV GUI windows require a display, so the scripts won't run on a headless server without extra setup.

## Roadmap

Natural next steps for the project:

- Detect the helipad's "H" marking and circular boundary specifically (e.g. `HoughCircles`, shape approximation with `approxPolyDP`)
- Convert the pixel offset into a steering or correction signal
- Run the pipeline on live video or a camera feed
- Replace hardcoded paths with `pathlib` and a command-line argument for the input image
- Add a `requirements.txt`

## License

No license has been specified yet. Consider adding one (e.g. MIT) if you want others to reuse the code.


##################################################################### LESSON 09 #######################################################################################

# ARES – Lesson 09
# Connected Components Analysis (OpenCV)

## 1. Learning Objectives

By the end of this lesson, we will understand:

1. Binary image creation.
2. Connected Components Analysis.
3. Component labelling.
4. Extracting object properties.
5. Bounding boxes and centroids.
6. Area-based object filtering.
7. Applications in automotive ADAS and computer vision.

---

## 2. Understanding Binary Images

A binary image contains only two pixel values:

- 0 – Black
- 255 – White

In this lesson, we create an image containing three separate white objects against a black background.

### Python Code

```python
image = np.zeros((400, 600), dtype=np.uint8)

cv2.rectangle(image, (50, 50), (150, 150), 255, -1)
cv2.circle(image, (300, 100), 50, 255, -1)
cv2.rectangle(image, (400, 200), (550, 350), 255, -1)
```

### Explanation

- `np.zeros()` creates a black image.
- `cv2.rectangle()` draws rectangular objects.
- `cv2.circle()` draws a circular object.
- `255` represents white.
- `-1` fills the complete shape.

**Observation:** The image contains three separate foreground objects.

---

## 3. Connected Components Analysis

Connected Components Analysis identifies separate connected regions in a binary image.

OpenCV groups neighbouring foreground pixels and assigns a unique label to each connected region.

### Python Code

```python
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(image)
```

### Four Returned Values

| Variable | Description |
|---|---|
| num_labels | Total number of labels, including background |
| labels | Label assigned to every pixel |
| stats | Measurements of each component |
| centroids | Centre coordinates of each component |

### Understanding Labels

Expected output:

```text
Number of labels: 4
Unique labels: [0 1 2 3]
```

| Label | Description |
|---|---|
| 0 | Background |
| 1 | First rectangle |
| 2 | Circle |
| 3 | Second rectangle |

Why four labels?

Because OpenCV also considers the background as a component.

**Connectivity:** OpenCV uses 8-connectivity by default. Horizontal, vertical and diagonal neighbouring foreground pixels can belong to the same component.

---

## 4. Visualizing Component Labels

### Python Code

```python
label_image = (labels * 80).astype(np.uint8)

plt.imshow(label_image, cmap='nipy_spectral')
plt.title("Connected Components - Labels")
plt.axis("off")
plt.show()
```

### Explanation

The labels array contains integer values representing individual components.

Multiplying by 80 makes the label values easier to distinguish visually.

| Original Label | Visualization Value |
|---|---|
| 0 | 0 |
| 1 | 80 |
| 2 | 160 |
| 3 | 240 |

The colour map converts these values into different displayed colours.

**Important:** Colours are only for visualization. The actual labels remain 0, 1, 2 and 3.

### Checking Individual Labels

```python
print("Unique labels:", np.unique(labels))

print("Label at object 1:", labels[100, 100])
print("Label at object 2:", labels[100, 300])
print("Label at object 3:", labels[250, 450])
```

Expected output:

```text
Unique labels: [0 1 2 3]
Label at object 1: 1
Label at object 2: 2
Label at object 3: 3
```

**Important:** NumPy image indexing follows `[y, x]`, whereas OpenCV drawing coordinates use `(x, y)`.

---

## 5. Extracting Object Properties

Connected Components provides useful measurements for every detected object.

The `stats` array contains:

| Property | OpenCV Constant | Description |
|---|---|---|
| X | CC_STAT_LEFT | Left starting coordinate |
| Y | CC_STAT_TOP | Top starting coordinate |
| Width | CC_STAT_WIDTH | Bounding box width |
| Height | CC_STAT_HEIGHT | Bounding box height |
| Area | CC_STAT_AREA | Number of foreground pixels |

The centroid contains the geometric centre coordinates.

### Python Code

```python
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
```

We start the loop from 1 because label 0 represents the background.

### Expected Results

| Object | X | Y | Width | Height | Area |
|---|---:|---:|---:|---:|---:|
| Rectangle 1 | 50 | 50 | 101 | 101 | 10,201 |
| Circle | 250 | 50 | 101 | 101 | 7,845 |
| Rectangle 2 | 400 | 200 | 151 | 151 | 22,801 |

### Important Observation

The circle and first rectangle have identical bounding box dimensions, but different areas.

This demonstrates that bounding box dimensions alone cannot describe the actual shape of an object.

---

## 6. Understanding Centroids

A centroid represents the geometric centre of a connected component.

For example:

- Rectangle 1: (100, 100)
- Circle: (300, 100)
- Rectangle 2: (475, 275)

Centroids help determine the approximate position of detected objects.

They are useful in object tracking, positioning and image analysis.

---

## 7. Drawing Bounding Boxes and Centroids

We can visualize the detected objects by drawing:

- Green rectangle – Bounding box
- Red dot – Centroid
- Blue text – Object ID

### Python Code

```python
output = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

for i in range(1, num_labels):

    x = stats[i, cv2.CC_STAT_LEFT]
    y = stats[i, cv2.CC_STAT_TOP]

    w = stats[i, cv2.CC_STAT_WIDTH]
    h = stats[i, cv2.CC_STAT_HEIGHT]

    cx, cy = centroids[i]

    cv2.rectangle(
        output,
        (x, y),
        (x+w, y+h),
        (0, 255, 0),
        2
    )

    cv2.circle(
        output,
        (int(cx), int(cy)),
        5,
        (0, 0, 255),
        -1
    )

    cv2.putText(
        output,
        f"Object {i}",
        (x, y-10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 0, 0),
        2
    )

plt.figure(figsize=(10, 6))
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title("Connected Components - Object Detection")
plt.axis("off")
plt.show()
```

**Note:** We convert the grayscale image into BGR so that coloured annotations can be drawn.

---

## 8. Area-Based Object Filtering

In practical computer vision, images may contain unwanted small regions or noise.

We can filter detected components using their area.

### Python Code

```python
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

        cv2.rectangle(
            output,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

        cv2.circle(
            output,
            (int(cx), int(cy)),
            5,
            (0, 0, 255),
            -1
        )

        print(f"Object {i} detected | Area: {area}")

plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title("Area-Based Object Filtering")
plt.axis("off")
plt.show()
```

### Expected Results

Minimum area = 8,000 pixels.

| Object | Area | Result |
|---|---:|---|
| Rectangle 1 | 10,201 | Detected |
| Circle | 7,845 | Filtered |
| Rectangle 2 | 22,801 | Detected |

Only two objects should have bounding boxes.

**Concept:** Area-based filtering removes components that do not meet the specified minimum area.

---

## 9. Automotive ADAS Applications

Connected Components Analysis can be useful in several computer vision applications.

### 9.1 Parking Assistance
Identifying separate foreground regions in thresholded obstacle images.

### 9.2 Road Segmentation
Separating connected regions of road markings and other foreground features.

### 9.3 Noise Removal
Removing small unwanted regions from binary images.

### 9.4 Autonomous Drone Landing
Identifying separate candidate landing regions and calculating their centres.

**Limitation:** Connected Components does not understand object identity. It only groups connected foreground pixels. Actual vehicle and pedestrian recognition requires more advanced methods such as YOLO and semantic segmentation.

---

## 10. Important Concepts to Remember

| Concept | Purpose |
|---|---|
| Binary Image | Separates foreground and background |
| Connected Components | Identifies separate connected regions |
| Labels | Assigns IDs to individual components |
| Stats | Extracts object measurements |
| Centroid | Finds the geometric centre |
| Bounding Box | Defines object boundaries |
| Area Filtering | Selects objects based on pixel area |

---

## 11. Knowledge Check

1. If an image contains five separate white objects, how many labels will OpenCV return?
   - Answer: 6, including background.

2. What does `CC_STAT_AREA` calculate?
   - Answer: Number of foreground pixels in the component.

3. What happens when two objects touch diagonally under default 8-connectivity?
   - Answer: They may be considered one connected component.

---

## 12. Lesson Completion

**ARES – Lesson 09: Connected Components Analysis**

Topics covered:

- Binary image creation
- Connected component labelling
- Understanding the labels array
- Extracting object statistics
- Calculating centroids
- Drawing bounding boxes
- Area-based object filtering
- Automotive ADAS applications

**Next Lesson: Lesson 10 – Image Segmentation using Thresholding and Adaptive Thresholding.**

---

*Project: ARES – Autonomous Robotics and Embedded Systems*  
*Technology: Python, OpenCV, NumPy and Matplotlib*
