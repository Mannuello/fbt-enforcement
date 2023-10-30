import cv2
import numpy as np
import pytesseract
import logging
from PIL import Image


logger = logging.getLogger(__name__)


def read_plate_from_image(image_path: str) -> str | None:
    """Reads and returns plate numbers from random plate images"""
    try:
        if image_path:
            # Read image using opencv
            img = cv2.imread(image_path)

            # Convert to gray
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Apply dilation and erosion to remove some noise
            kernel = np.ones((1, 1), np.uint8)
            gray = cv2.dilate(gray, kernel, iterations=1)
            gray = cv2.erode(gray, kernel, iterations=1)

            # Apply Gaussian blur to smooth out the edges
            gray = cv2.GaussianBlur(gray, (5, 5), 0)

            # Apply thresholding to get a binary image
            _, binary_img = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
            )

            # Define your configuration settings
            myconfig = r"--psm 9 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

            # Recognize text with Tesseract for Python
            plate_number = pytesseract.image_to_string(
                Image.fromarray(binary_img), config=myconfig
            )
            # Remove the first character from result, erroneous
            plate_number = plate_number[1:]
            plate_number = plate_number.strip()
            logger.info(f"Plate number: {plate_number} read from path: {image_path}")
            return plate_number
        else:
            logger.warn(f"Unable to retrieve plate number from non-existent path")
            return None
    except Exception as e:
        logger.error(
            f"{e} has occured while trying to read plate image path: {image_path}"
        )
