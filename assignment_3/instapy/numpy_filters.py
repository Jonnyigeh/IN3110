"""numpy implementation of image filters"""

import numpy as np
import time
from PIL import Image
from typing import Optional


def numpy_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    gray_image = np.empty_like(image)
    # Hint: use numpy slicing in order to have fast vectorized code
    # Return image (make sure it's the right type!)
    f = lambda x: ( x[0] * 0.21 + x[1] * 0.72 + x[2] * 0.07 ) * np.array([1,1,1]) #/ 3
    gray_image = np.asarray(np.apply_along_axis(f, 2, image), dtype="uint8")
    return gray_image


def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
        k (float): amount of sepia filter to apply (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    (note: implementing 'k' is a bonus task,
    you may ignore it for Task 9)

    Returns:
        np.array: sepia_image
    """

    if not 0 <= k <= 1:
        # validate k (optional)
        raise ValueError(f"k must be between [0-1], got {k=}")
    def f(x):
        R = x[0]
        G = x[1]
        B = x[2]
        newR = int( R * 0.393 + G * 0.769 + B * 0.189 )
        newG = int( R * 0.349 + G * 0.686 + B * 0.168 )
        newB = int( R * 0.272 + G * 0.534 + B * 0.131 )
        if newR > 255:
            newR = 255

        if newG > 255:
            newG = 255

        if newB > 255:
            newB = 255
        return np.array([newR,newG,newB])

    sepia_image = np.empty_like(image)
    sepia_image = np.asarray(np.apply_along_axis(f, 2, image), dtype="uint8")

    # define sepia matrix (optional: with `k` tuning parameter for bonus task 13)
    # sepia_matrix = ...

    # HINT: For version without adaptive sepia filter, use the same matrix as in the pure python implementation
    # use Einstein sum to apply pixel transform matrix
    # Apply the matrix filter


    # Check which entries have a value greater than 255 and set it to 255 since we can not display values bigger than 255
    # Return image (make sure it's the right type!)
    breakpoint()
    return sepia_image

if __name__=="__main__":
    t1 = time.time()
    im = Image.open(".././rain.jpg")
    pixel = np.asarray(im)
    sepia_im = numpy_color2sepia(pixel)
    t2 = time.time()
    breakpoint()
