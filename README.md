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
