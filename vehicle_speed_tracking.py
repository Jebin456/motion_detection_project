import cv2
import time

# Set real-world distance (in meters) between the two lines
DISTANCE_BETWEEN_LINES = 10

# Initialize video
cap = cv2.VideoCapture("vehicle_video.mp4")  # Replace with 0 for webcam

# Line positions (in pixels)
LINE_POSITION_1 = 200
LINE_POSITION_2 = 400

vehicle_entry_times = {}
vehicle_id = 0
speeds = []

# Background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape
    fgmask = fgbg.apply(frame)
    _, thresh = cv2.threshold(fgmask, 250, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 1000:
            continue

        (x, y, w, h) = cv2.boundingRect(cnt)
        cx = x + w // 2
        cy = y + h // 2

        # Draw vehicle box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Line crossing logic
        if LINE_POSITION_1 - 2 < cy < LINE_POSITION_1 + 2:
            vehicle_entry_times[vehicle_id] = time.time()

        elif LINE_POSITION_2 - 2 < cy < LINE_POSITION_2 + 2 and vehicle_id in vehicle_entry_times:
            elapsed_time = time.time() - vehicle_entry_times[vehicle_id]
            speed = DISTANCE_BETWEEN_LINES / elapsed_time * 3.6  # m/s to km/h
            speeds.append(speed)
            cv2.putText(frame, f"Speed: {speed:.2f} km/h", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            del vehicle_entry_times[vehicle_id]
            vehicle_id += 1

    # Draw reference lines
    cv2.line(frame, (0, LINE_POSITION_1), (width, LINE_POSITION_1), (255, 0, 0), 2)
    cv2.line(frame, (0, LINE_POSITION_2), (width, LINE_POSITION_2), (255, 0, 0), 2)

    cv2.imshow("Vehicle Speed Detection", frame)
    key = cv2.waitKey(30)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
