import threading
import cv2
import numpy as np
import pytesseract  # type: ignore
import logging
from PIL import Image
from queue import Queue

logger = logging.getLogger(__name__)


def read_plate_from_image(image_path: str, output_queue: Queue):
    if not image_path:
        logger.warning("No image path provided")
        output_queue.put(None)
        return

    try:
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
        _, binary_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

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
        output_queue.put(plate_number)
    except Exception as e:
        logger.error(
            f"{e} has occurred while trying to read plate image path: {image_path}"
        )
        output_queue.put(None)


def process_images(image_paths):
    output_queue = Queue()
    threads = []

    for image_path in image_paths:
        thread = threading.Thread(
            target=read_plate_from_image, args=(image_path, output_queue)
        )
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    results = []
    while not output_queue.empty():
        results.append(output_queue.get())

    return results
