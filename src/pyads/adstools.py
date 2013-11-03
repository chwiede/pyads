
def HexBlock(data, width = 8):
    result = ''
    i = 0
    
    for c in data:
        if (i == width):
            result += "\n"
            i = 0                

        result += "%02x " % ord(c)
        i += 1
    
    return result