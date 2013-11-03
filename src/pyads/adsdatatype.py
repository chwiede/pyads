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
    
    
    __packmapping__ = {
        Int8: 'b',
        UInt8: 'B',
        Int16: 'h',
        UInt16: 'H',
        Int32: 'i',
        UInt32: 'I',
        Int64: 'q',
        UInt64: 'Q',
        Float: 'f',
        Double: 'd',
        Bool: '?',
        String: None
    }
    
    
    __sizemapping__ = {
        Int8: 1,
        UInt8: 1,
        Int16: 2,
        UInt16: 2,
        Int32: 4,
        UInt32: 4,
        Int64: 8,
        UInt64: 8,
        Float: 4,
        Double: 8,
        Bool: 1,
        String: 80
    }
    
    
    @staticmethod
    def GetSize(adsDatatype):
        return AdsDatatype.__sizemapping__.get(adsDatatype, 0)
    
    
    @staticmethod
    def GetPackFormat(adsDatatype):
        return AdsDatatype.__packmapping__.get(adsDatatype, None)
           
    
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
    def UnPackFrom(adsDatatype, byteBuffer, offset):
        
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
        
