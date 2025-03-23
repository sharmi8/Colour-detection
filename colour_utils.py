import numpy as np
import cv2

def get_limits(color):
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]

    hue_range = 8
    sat_lower = 120
    sat_upper = 255
    val_lower = 190
    val_upper = 255

    if hue >= 165:
        lowerLimit = np.array([hue - hue_range, sat_lower, val_lower], dtype=np.uint8)
        upperLimit = np.array([180, sat_upper, val_upper], dtype=np.uint8)
    elif hue <= hue_range:
        lowerLimit = np.array([0, sat_lower, val_lower], dtype=np.uint8)
        upperLimit = np.array([hue + hue_range, sat_upper, val_upper], dtype=np.uint8)
    else:
        lowerLimit = np.array([hue - hue_range, sat_lower, val_lower], dtype=np.uint8)
        upperLimit = np.array([hue + hue_range, sat_upper, val_upper], dtype=np.uint8)

    return lowerLimit, upperLimit
