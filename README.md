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
