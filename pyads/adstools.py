
def HexBlock(data, width = 8):
    result = ''
    i = 0
    
    for byte in data:
        if (i == width):
            result += "\n"
            i = 0
            
        char = ord(byte) if isinstance(byte, str) else byte
        result += "%02x " % char
        i += 1
    
    return result