import numpy as np
import pytesseract
from PIL import Image
import cv2
import os


def read_plate_from_image(image_path: str) -> str:
    """Reads and returns plate numbers from random plate images"""
    # Read image using opencv
    img = cv2.imread(image_path)

    # Extract the file name without the file extension
    file_name = os.path.splitext(os.path.basename(image_path))[0]

    # Convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    gray = cv2.dilate(gray, kernel, iterations=1)
    gray = cv2.erode(gray, kernel, iterations=1)

    # Apply Gaussian blur to smooth out the edges
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply thresholding to get a binary image
    _, binary_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Define your configuration settings
    myconfig = r"--psm 9 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    # Recognize text with Tesseract for Python
    result = pytesseract.image_to_string(Image.fromarray(binary_img), config=myconfig)
    # Remove the first character from result, erroneous
    result = result[1:]
    return result


def get_single_car_data(plate_number: str, car_records: list) -> dict:
    """Uses a plate number to find an associated car record and returns a single instance"""
    for record in car_records:
        if record.get("plate_number") == plate_number:
            return record
    return {}
