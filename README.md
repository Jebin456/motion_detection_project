# motion_detection_project


---

# 🎥 Motion Detection Project

A simple yet effective motion detection system built using **Python** and **OpenCV**. This project detects movement in real-time video streams or from a webcam and highlights areas where motion is detected.

---

## 🔍 Features

- Real-time motion detection from webcam or video file
- Draws bounding boxes around moving objects
- Logs timestamps when motion starts and stops
- Adjustable sensitivity (via frame delta threshold)

---

## 📦 Requirements

Before running the project, ensure you have the following installed:

- Python 3.x
- OpenCV (`cv2`)
- imutils

Install dependencies using:

```bash
pip install opencv-python imutils
```

---

## ▶️ How to Run

### For Webcam Input:
```bash
python motion_detector.py
```

### For Video File Input:
Edit the script and provide the path to your video file:
```python
vs = cv2.VideoCapture("your_video.mp4")
```

Then run:
```bash
python motion_detector.py
```

> Press `q` to quit the program during execution.

---

## 📁 Project Structure

```
motion-detection-project/
│
├── motion_detector.py       # Main motion detection script
├── requirements.txt         # Required Python packages
├── README.md                # This file
└── .gitignore               # Files/folders to ignore on Git
```

---

## 📝 Notes

- The detector uses background subtraction and frame differencing to detect motion.
- Sensitivity can be adjusted by changing the threshold value in the code.
- Bounding boxes highlight regions with motion.
- Logs are printed to the console indicating when motion starts/stops.

---

## 📸 Screenshot (Optional)

Include a screenshot of the motion detection window if available. It helps users understand what to expect.

Example:

![Motion Detection Screenshot](screenshot.png)

> 📌 *Note: If you're adding screenshots, place them in an `assets/` or `screenshots/` folder and update the path accordingly.*

---

## 📄 License

MIT License – see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributions

Contributions are welcome! Feel free to open issues or submit pull requests for improvements such as:

- Saving logs to a file
- Adding email alerts on motion detection
- Supporting multiple cameras

---


# 🚗 Vehicle Speed Detection using OpenCV

This project uses OpenCV to detect moving vehicles in a video and calculate their speed based on the time they take to travel between two fixed points. It’s a basic implementation using background subtraction and frame timing.

## 📷 How It Works

1. A video feed (or webcam) is analyzed using OpenCV.
2. Two horizontal lines are drawn in the frame at known vertical positions.
3. When a vehicle crosses the first line, the timestamp is recorded.
4. When the same vehicle crosses the second line, the time difference is calculated.
5. Using the known distance between the lines, speed is computed in km/h.

## 🛠️ Requirements

- Python 3.x
- OpenCV

Install dependencies:

```bash
pip install -r requirements.txt
````

## 🧾 Files

* `vehicle_speed_detector.py`: Main script to run speed detection.
* `requirements.txt`: Python dependencies.
* `vehicle_video.mp4`: (Optional) Input video file. Replace with your own.

## 🧠 Formula Used

Speed = (Distance / Time) × 3.6
*(Converts m/s to km/h)*

Where:

* Distance = Real-world distance between the two lines (in meters)
* Time = Time in seconds between line crossings

## 🖼 Example

Two horizontal lines are shown on the video frame. Vehicles crossing both lines will have their speed calculated and displayed in real-time.

## 📂 How to Use

1. Place your video file in the project folder.
2. Open `vehicle_speed_detector.py` and change this line:

   ```python
   cap = cv2.VideoCapture("vehicle_video.mp4")
   ```

   Replace `"vehicle_video.mp4"` with your video filename or use `0` for webcam.
3. Adjust the following values to match your scenario:

   * `DISTANCE_BETWEEN_LINES` (meters)
   * `LINE_POSITION_1`, `LINE_POSITION_2` (pixels)
4. Run the script:

```bash
python vehicle_speed_detector.py
```

Press `q` to quit the program.

## ⚠️ Disclaimer

This is a basic educational project. For real-world applications, consider using:

* Object tracking (e.g., OpenCV trackers)
* Object detection (YOLO, MobileNet, etc.)
* Camera calibration for real distance estimation

## 📝 License

This project is open-source and free to use under the MIT License.

```

---

Would you like me to package this into a ready-to-upload GitHub folder (with all files)?
```

