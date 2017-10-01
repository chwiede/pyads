import struct


class AdsDatatype:

    Custom = 0x00
    Int8 = 0x01
    UInt8 = 0x02
    Int16 = 0x03
    UInt16 = 0x04
    Int32 = 0x05
    UInt32 = 0x06
    Int64 = 0x07
    UInt64 = 0x08
    Float = 0x09
    Double = 0x0A
    Bool = 0x0B
    String = 0x0C


    __infomapping__ = {
        Int8:   ('b', 1, 'Int8'),
        UInt8:  ('B', 1, 'UInt8'),
        Int16:  ('h', 2, 'Int16'),
        UInt16: ('H', 2, 'UInt16'),
        Int32:  ('i', 4, 'Int32'),
        UInt32: ('I', 4, 'UInt32'),
        Int64:  ('q', 8, 'Int64'),
        UInt64: ('Q', 8, 'UInt64'),
        Float:  ('f', 4, 'Float'),
        Double: ('d', 8, 'Double'),
        Bool:   ('?', 1, 'Bool'),
        String: (None, 80, 'String')
    }



    @staticmethod
    def GetPackFormat(adsDatatype):
        return AdsDatatype.__infomapping__.get(adsDatatype)[0]


    @staticmethod
    def GetSize(adsDatatype):
        return AdsDatatype.__infomapping__.get(adsDatatype)[1]


    @staticmethod
    def GetName(adsDatatype):
        return AdsDatatype.__infomapping__.get(adsDatatype)[2]


    @staticmethod
    def Pack(value, adsDatatype):

        packFmt = AdsDatatype.GetPackFormat(adsDatatype)

        if(packFmt != None):
            return struct.pack(packFmt, value)
        else:
            return value


    @staticmethod
    def PackInto(adsDatatype, byteBuffer, offset, value):

        packFmt = AdsDatatype.GetPackFormat(adsDatatype)

        if(packFmt == None):
            raise Exception("no pack format found.")

        struct.pack_into(packFmt, byteBuffer, offset, value)


    @staticmethod
    def UnpackFrom(adsDatatype, byteBuffer, offset):

        packFmt = AdsDatatype.GetPackFormat(adsDatatype)

        if(packFmt == None):
            raise Exception("no pack format found.")

        return struct.unpack_from(packFmt, byteBuffer, offset)[0]


    @staticmethod
    def Unpack(value, adsDatatype):

        packFmt = AdsDatatype.GetPackFormat(adsDatatype)

        if(packFmt != None):
            return struct.unpack(packFmt, value)[0]
        else:
            return value

