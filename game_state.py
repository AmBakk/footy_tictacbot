import cv2
import numpy as np


def get_game_state(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to HSV (Hue, Saturation, Value) color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Focus on the central region where the shirt is likely to be
    h, w, _ = hsv_image.shape
    shirt_region = hsv_image[int(h*0.25):int(h*0.75), int(w*0.25):int(w*0.75)]

    # Define color range for detecting blue (O)
    blue_lower = np.array([100, 100, 50])
    blue_upper = np.array([140, 255, 255])

    # Define color range for detecting white (X)
    white_lower = np.array([0, 0, 160])
    white_upper = np.array([180, 40, 255])

    # Create masks for blue and white colors
    blue_mask = cv2.inRange(shirt_region, blue_lower, blue_upper)
    white_mask = cv2.inRange(shirt_region, white_lower, white_upper)

    # Count the number of pixels in each mask
    blue_pixels = cv2.countNonZero(blue_mask)
    white_pixels = cv2.countNonZero(white_mask)

    # Determine the color with the most pixels
    if blue_pixels > white_pixels:
        return 'O'
    elif white_pixels > blue_pixels:
        return 'X'
    else:
        return ''
