import sys
import cv2
import numpy as np

class RLE:
    def __init__(this):
        this.space_count = 0

        this.pixelList_buffer = ""
        this.duplicate_buffer = ""
        this.duplicate_count = 0

        this.row = []

        this.row_count = 1
        this.duplicate_sum = 0

        # Show full ndarray
        np.set_printoptions(threshold=sys.maxsize)

    def encode(this, image):
        encode_image = []

        height, width, _ = image.shape
        for row in range(height):
            # Reset count every new row (height)
            count = 1

            # No compare with last column
            for column in range(width - 1):
                # Check if current column equar to next column (Check every elements in array [B, G, R])
                if (image[row, column] == image[row, column+1]).all():
                    count = count + 1
                else:
                    encode_image.extend([image[row, column], count])
                    count = 1

            # Add the last column
            encode_image.extend([image[row, column + 1], count])

            # '-1' represent to end of image column (Similar with '\n' or '\r''\n')
            encode_image.append(-1)

        # Return result with 1-dimensional array
        return encode_image
    
    # Save encode image to file
    def saveResult(this, encode_image, dataType, eof, filepath):
        ##############################################################
        #             Encode image is 1-dimensional array           #
        # Height & Width of original image not equar to encode_image #
        ##############################################################

        with open(filepath, 'w') as file:
            for item in encode_image:
                # Check type of item
                if isinstance(item, dataType):
                    # If item is ... then Convert array to string
                    pixel  = ' '.join(str(val) for val in item)
                    file.write(pixel + ' ')
                elif item == -1:
                    # If item is '-1' mean End of image column then go to new line
                    file.write('\n')
                else:
                    # This statement represent to Number of repeating image pixels
                    file.write(str(item) + ' ')

            # Add costom End of file
            file.write(eof)

    def parseRleImage(this, encode_image, varControlFunc=lambda : 0, varAccessFunc=lambda pixelList: 0):
        decode_image = []

        for c in encode_image:
            # Count space
            if c == ' ':
                this.space_count = this.space_count + 1

            # New columnc
            if c == '\n':
                this.row_count = this.row_count + 1
                this.duplicate_sum = 0

                c.rstrip()
                # Add row to main image
                decode_image.extend([this.row])
                # Clear pixel list in previous row
                this.row = []

            # Get duplicate count
            if this.space_count >= 3:
                this.duplicate_buffer = this.duplicate_buffer + c

            # Complete 1 Pixel set
            if this.space_count == 4:
                varControlFunc()

                this.duplicate_count = int(this.duplicate_buffer.strip())
                pixelList = [float(val) for val in this.pixelList_buffer.split()]
                this.duplicate_sum = this.duplicate_sum + this.duplicate_count

                varAccessFunc(pixelList)

                # Duplicate pixel
                for i in range(this.duplicate_count):
                    # Add pixel to row
                    this.row.extend([pixelList])

                this.space_count = 0
                this.pixelList_buffer = ""
                this.duplicate_buffer = ""
                this.duplicate_count = 0
            elif this.space_count < 3:
                # Add each character from serial port to pixel buffer
                this.pixelList_buffer = this.pixelList_buffer + c.replace('\n', '')

        # Convert list to np.ndarray type
        decode_image = np.array(decode_image)
        # Convert image depth
        decode_image = decode_image.astype(np.uint8)
        return decode_image

    def loadEncodeImage(this, path):
        with open(path, 'r') as file:
            image = file.read()

        return image

    def saveDecodeImage(this, decode_image, path):
        with open(path, 'w') as file:
            file.write(decode_image)

        return decode_image
    
    def showImage(this, image):
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
