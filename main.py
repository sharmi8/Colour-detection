import cv2
import numpy as np
from PIL import Image
from colour_utils import get_limits

cap = cv2.VideoCapture(0)

# Define yellow color in BGR and convert it to HSV
yellow_bgr = np.uint8([[[0, 255, 255]]])  
yellow_hsv = cv2.cvtColor(yellow_bgr, cv2.COLOR_BGR2HSV)[0][0]

lowerLimit, upperLimit = get_limits(yellow_hsv)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)  # Show the mask for debugging

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


