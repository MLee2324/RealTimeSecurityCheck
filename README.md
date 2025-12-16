# YOLOv8 Webcam People Counter

This project implements a real-time people counting system using a **webcam feed**, **YOLOv8**, and **OpenCV**. The system detects and tracks people in each frame and counts how many individuals enter or exit the scene based on crossing a predefined vertical line.

This version differs from the video-based implementation by operating directly on a **live camera stream**, making it suitable for real-time monitoring scenarios.

---

## Features

* Real-time person detection using YOLOv8
* Persistent object tracking with unique IDs
* Entry and exit counting via line-crossing logic
* Live webcam input
* On-screen counters for entered and exited counts
* Bounding boxes, centroids, and tracking IDs drawn on frames

---

## How It Works

1. Frames are captured from the webcam using OpenCV
2. YOLOv8 detects people (class ID 0) in each frame
3. The tracker assigns a persistent ID to each detected person
4. The centroid of each bounding box is calculated
5. Previous and current centroid positions are compared
6. If a centroid crosses the vertical reference line:

   * Left to right indicates an entry
   * Right to left indicates an exit
7. Counters are updated and displayed on the video feed

---

## Project Structure

```
project-root/
│
├── main.py              # Webcam-based detection and tracking loop
├── drawers.py           # Drawing utilities and line-crossing logic
├── yolov8m.pt           # YOLOv8 pretrained weights
```

---

## How to Run

### 1. Install dependencies

```bash
pip install ultralytics opencv-python
```

### 2. Run the program

```bash
python main.py
```

Press **Q** to quit the application.

---

## Configuration

### Webcam settings

In `main.py`, webcam resolution can be adjusted:

```python
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 700)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
```

### Counting line position

The vertical line used for counting is defined as:

```python
line_x = 340
```

Adjust this value based on camera placement and scene layout.

---

## Key Files Explained

### main.py

* Loads the YOLOv8 model
* Captures frames from the webcam
* Runs detection and tracking logic
* Displays live counters and visual overlays

### drawers.py

* Draws bounding boxes and tracking IDs
* Maintains centroid history for each track ID
* Detects entry and exit events
* Renders counters and UI elements

---

## Limitations

* Assumes a single vertical entry/exit line
* Performance depends on webcam quality and hardware
* No automatic region-of-interest selection
* Not optimized for crowded or overlapping scenes

---

## Possible Improvements

* Add dynamic ROI or adjustable counting lines
* Support multiple entry and exit zones
* Integrate more advanced trackers (e.g., Deep SORT, ByteTrack)
* Log counts to a file or database
* Add support for multiple cameras

---

## Author

Built as a personal computer vision project using YOLOv8 and OpenCV.

---

## Notes

This implementation prioritizes clarity and learning over production-level robustness and is intended for educational and experimental use.
