class AlphaEn:
    def __init__(this):
        this.alphaList = []

        # Initialize alphabet list
        for c in range(ord('A'), ord('Z')+1):
            this.alphaList.append(chr(c))

    def start(this, strDigit):
        buffer = []
        encode = ""
        stack = 0

        # Convert (str) to (char-list)
        strDigitList = this.split(strDigit)

        if len(strDigitList) == 1:
            return this.toAlpha(strDigitList)
        
        # For e in (char-list)
        for e in strDigitList:
            buffer.append(e)
            stack = stack + 1

            if stack == 2:
                # Convert (char-list) and Check if (char-list) is more than 25
                if this.union(buffer) > 25:
                    encode = encode + this.toAlpha(buffer[0])
                    buffer.pop(0)
                    stack = 1
                else:
                    encode = encode + this.toAlpha([''.join(buffer)])
                    buffer = []

        if len(buffer)%2 != 0:
            encode = encode + this.toAlpha([strDigitList[-1]])

        return encode

    # Split (str)Digit to (char-list)Digit
    def split(this, strDigit):
        buffer = []

        for i in range(len(strDigit)):
            buffer.append(strDigit[i])
        return buffer

    # Union (char-list) to (int)
    def union(this, numberCharacters):
        return int(''.join(numberCharacters))

    def toAlpha(this, numberCharacters):
        buffer = []

        for e in numberCharacters:
            index = int(e)
            buffer.append(this.alphaList[index])

        return ''.join(buffer)
    
    def toDigit(this, alpha):
        buffer = []
        charList = this.split(alpha)

        for e in charList:
            buffer.append(str(this.alphaList.index(e)))

        return ''.join(buffer)


