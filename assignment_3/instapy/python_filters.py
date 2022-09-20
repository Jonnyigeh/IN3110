"""pure Python implementation of image filters"""

import numpy as np
import time
from PIL import Image

def python_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    gray_image = np.empty_like(image)
    # iterate through the pixels, and apply the grayscale transform
    for i in range(np.shape(image)[0]):
        for j in range(np.shape(image)[1]):
            weighted_avg = (image[i][j][0] * 0.21 + image[i][j][1] * 0.72
                            + image[i][j][2] * 0.07) #/ 3
            gray_image[i][j][0] = weighted_avg
            gray_image[i][j][1] = weighted_avg
            gray_image[i][j][2] = weighted_avg

    return gray_image


def python_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image)

    # Iterate through the pixels
    # applying the sepia matrix
    for i in range(np.shape(image)[0]):
        for j in range(np.shape(image)[1]):
            R = image[i][j][0]
            G = image[i][j][1]
            B = image[i][j][2]
            sepia_R = int( R * 0.393 + G * 0.769 + B * 0.189 )
            sepia_G = int( R * 0.349 + G * 0.686 + B * 0.168 )
            sepia_B = int( R * 0.272 + G * 0.534 + B * 0.131 )
            if sepia_R > 255:
                sepia_R = 255

            if sepia_G > 255:
                sepia_G = 255

            if sepia_B > 255:
                sepia_B = 255

            sepia_image[i][j][0] = sepia_R
            sepia_image[i][j][1] = sepia_G
            sepia_image[i][j][2] = sepia_B

    # Return image
    # don't forget to make sure it's the right type!
    return sepia_image

if __name__=="__main__":
    t1 = time.time()
    im = Image.open(".././rain.jpg")
    pixel = np.asarray(im)
    sepia_im = python_color2sepia(pixel)
    t2 = time.time()
    breakpoint()
