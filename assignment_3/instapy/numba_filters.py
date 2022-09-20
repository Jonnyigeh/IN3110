"""numba-optimized filters"""
import numpy as np
import time
from numba import jit
from PIL import Image


@jit(nopython=True)
def numba_color2gray(image: np.array) -> np.array:
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


def numba_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image)
    # Iterate through the pixels
    # applying the sepia matrix

    ...

    # Return image
    # don't forget to make sure it's the right type!
    return sepia_image


if __name__ == "__main__":
    t1 = time.time()
    im = Image.open(".././rain.jpg")
    pixel = np.asarray(im)
    gray_im = numba_color2gray(pixel)
    t2 = time.time()
    breakpoint()
