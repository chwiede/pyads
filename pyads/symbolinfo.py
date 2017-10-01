from .adsdatatype import AdsDatatype

class SymbolInfo:


    def __init__(self, name, indexGroup, indexOffset, adsDatatype, bitOffset = 0):
        self.Name = name
        self.IndexGroup = indexGroup
        self.IndexOffset = indexOffset
        self.AdsDatatype = adsDatatype
        self.BitOffset = bitOffset


    Name = ''

    IndexGroup = 0

    IndexOffset = 0

    BitOffset = 0

    AdsDatatype = AdsDatatype.Custom

    Value = None


    def WriteTo(self, byteBuffer):

        # byte shift needed, if bool!
        if (self.AdsDatatype == AdsDatatype.Bool):
            currentByte = AdsDatatype.UnpackFrom(AdsDatatype.UInt8, byteBuffer, self.IndexOffset)
            if (self.Value):
                newByte = currentByte | (1 << self.BitOffset)
            else:
                newByte = currentByte & ~(1 << self.BitOffset) & 0xF

            AdsDatatype.PackInto(AdsDatatype.UInt8, byteBuffer, self.IndexOffset, newByte)

        else:
            AdsDatatype.PackInto(self.AdsDatatype, byteBuffer, self.IndexOffset, self.Value)



    def ReadFrom(self, byteBuffer):

        if (self.AdsDatatype == AdsDatatype.Bool):
            result = AdsDatatype.UnpackFrom(AdsDatatype.UInt8, byteBuffer, self.IndexOffset)
            result = ((result & (1 << self.BitOffset)) == True)
        else:
            result = AdsDatatype.UnpackFrom(self.AdsDatatype, byteBuffer, self.IndexOffset)

        self.Value = result
        return result



    def __str__(self):
        return "%s [%s] (%08x, %08x%s)" % (
            self.Name,
            AdsDatatype.GetName(self.AdsDatatype),
            self.IndexGroup,
            self.IndexOffset,
            (".%s" % self.BitOffset) if self.AdsDatatype == AdsDatatype.Bool else ''
        )