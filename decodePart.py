from Modules.rle import RLE
from Modules.alphaEn import AlphaEn

rle = RLE()
alphaEn = AlphaEn()

def rleDecode(imagePath):
    # Load REL image
    rle_image = rle.loadEncodeImage(imagePath)
    # Decode RLE image
    decode_image = rle.parseRleImage(rle_image)

    rle.showImage(decode_image)

def alphaDecode(encodeImagePath):
    # Load AlphaEn image
    alphaEn_image = rle.loadEncodeImage(encodeImagePath)

    #Decode AlphaEn image
    decode_image = rle.parseRleImage(
        encode_image=alphaEn_image,
        varControlFunc=controlFunc,
        # varAccessFunc=log
    )

    rle.showImage(decode_image)

def controlFunc():
    # Convert Duplicate count
    # print(f"Duplicate buffer alpha: {rle.duplicate_buffer.strip()}")
    rle.duplicate_buffer = alphaEn.toDigit(rle.duplicate_buffer.strip())
    # print(f"Duplicate buffer digit: {rle.duplicate_buffer.strip()}")

    # Convert Pixel
    buffer = []
    # print(f"Pixel buffer alpha: {rle.pixelList_buffer.split()}")
    for pixel in rle.pixelList_buffer.split():
        buffer.append(alphaEn.toDigit(pixel))
    rle.pixelList_buffer = ' '.join(buffer)
    # print(f"Pixel buffer digit: {rle.pixelList_buffer.split()}")

def log(pixelList):
    print(f"Row count: {rle.row_count}")
    print(f"Duplicate count: {rle.duplicate_count}")
    print(f"Duplicate sum: {rle.duplicate_sum}")
    print(f"Pixel list buffer: {rle.pixelList_buffer}")

    print("\n\n")

    for pixel in pixelList:
        if pixel > 255.0:
            print("\n\n [Error Pixel Length] \n\n")
            exit()

    if rle.duplicate_sum > 480:
        print("\n\n [Error Duplicate sum] \n\n")
        exit()