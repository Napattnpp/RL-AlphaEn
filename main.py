from encodePart import *
from decodePart import *

if __name__ == "__main__":
    '''
        1) Load normal image then Encode normal image with RLE and save RLE image
        2) Load RLE image then convert to normal image and show normal image
    '''
    # rlEncode()
    # rleDecode()

    '''
        1) Load normal image then Encode normal image with RLE and save RLE image
        2) Load RLE image then convert RLE image to AlphaEn image and save AlphaEn image
    '''
    alphaEncode(
        imagePath='',
        outputPath=''
    )
    alphaDecode(
        encodeImagePath=''
    )
