import cv2
import numpy as np

from Modules.rle import RLE
from Modules.alphaEn import AlphaEn

rle = RLE()
alphaEn = AlphaEn()

def rlEncode(imagePath, outputPath):
    # Load image
    image = cv2.imread(imagePath)
    # Encode image with RLE and Save encode image
    rle_image = rle.encode(image)
    rle.saveResult(
        encode_image=rle_image,
        dataType=np.ndarray,
        eof="!",
        filepath=outputPath
    )

alpha_image = []
pre_row_count = [1]
def alphaEncode(imagePath, outputPath):
    # Load image
    image = cv2.imread(imagePath)
    # Encode image with RLE and Save encode image
    rle_image = rle.encode(image)
    rle.saveResult(
        encode_image=rle_image,
        dataType=np.ndarray,
        eof="!",
        filepath=outputPath
    )

    # Load RLE image
    rle_image = rle.loadEncodeImage(outputPath)

    # Encode RLE image to AlphaEn
    rle.parseRleImage(
        encode_image=rle_image,
        varAccessFunc=accessFunc
    )

    # Save AlphaEncode to file
    rle.saveResult(
        encode_image=alpha_image,
        dataType=list,
        eof="\n!",
        filepath=outputPath
    )

def accessFunc(pixelList):
    buffer = []

    # Convert pixel list from (float) to (int)
    pixelList = [int(val) for val in pixelList]
    # Convert pixel list from (int) to (string)
    pixelList = [str(val) for val in pixelList]

    # Convert each pixel to (alphaEn) and Assign data to buffer
    for pixel in pixelList:
        buffer.append(alphaEn.start(pixel))

    if pre_row_count[0] != rle.row_count:
        alpha_image.append(-1)
        pre_row_count[0] = rle.row_count
    
    # Encode duplicate count with AlphaEn
    duplicate_alphaEn = alphaEn.start(str(rle.duplicate_count))
    alpha_image.extend([buffer, duplicate_alphaEn])