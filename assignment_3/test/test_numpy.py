from instapy.numpy_filters import numpy_color2gray, numpy_color2sepia
from PIL import Image
import numpy.testing as nt
import numpy as np
import random as rn

def test_color2gray(image, reference_gray):
    # run color2gray
    im = Image.open(".././rain.jpg")
    pixel = np.asarray(im)
    gray_im = numpy_color2gray(pixel)
    # check that the result has the right shape, type
    # assert uniform r,g,b values
    width = np.shape(gray_im)[0]
    height = np.shape(gray_im)[1]
    test_array = np.ones(10)
    for n in range(10):
        i = rn.randint(0, width-1)
        j = rn.randint(0, height-1)
        test_array[n] = gray_im[i][j][0] == (gray_im[i][j][1] and gray_im[i][j][2])

    assert (type(gray_im[1][1][1]) == np.uint8)
    assert (np.shape(pixel) == np.shape(gray_im))
    assert (all(test_array))

def test_color2sepia(image, reference_sepia):
    im = Image.open(".././rain.jpg")
    pixel = np.asarray(im)
    sepia_im = numpy_color2sepia(pixel)
    # check that the result has the right shape, type
    # verify some individual pixel samples
    # according to the sepia matrix
    width = np.shape(sepia_im)[0]
    height = np.shape(sepia_im)[1]
    test_array = np.ones(10)
    for n in range(10):
        i = rn.randint(0, width-1)
        j = rn.randint(0, height-1)
        R = pixel[i][j][0]
        G = pixel[i][j][1]
        B = pixel[i][j][2]
        sepia_R = int( R * 0.393 + G * 0.769 + B * 0.189 )
        sepia_G = int( R * 0.349 + G * 0.686 + B * 0.168 )
        sepia_B = int( R * 0.272 + G * 0.534 + B * 0.131 )
        if sepia_R > 255:
            sepia_R = 255

        if sepia_G > 255:
            sepia_G = 255

        if sepia_B > 255:
            sepia_B = 255

        test_array[n] = ( (sepia_im[i][j][0] == sepia_R) and
                    (sepia_im[i][j][1] == sepia_G) and
                (sepia_im[i][j][2] == sepia_B) )

    assert (type(sepia_im[1][1][1]) == np.uint8)
    assert (np.shape(pixel) == np.shape(sepia_im))
    assert (all(test_array))
