from struct import pack, unpack_from, calcsize

class BinaryParser:

    def __init__(self, byteData = b''):
        self.ByteData = byteData
        self.Position = 0


    ByteData = b''

    Position = 0


    def Append(self, fmt, value):
        self.ByteData = self.ByteData + pack(fmt, value)


    def Unpack(self, fmt):
        result = unpack_from(fmt, self.ByteData, self.Position)
        self.Position = self.Position + calcsize(fmt)

        return result[0]


    def ReadBytes(self, length):
        result = ''
        for i in range(length):
            result = result + chr(self.ReadByte())

        return result


    def WriteBytes(self, byteList):
        if (isinstance(byteList, str)):
            self.ByteData = self.ByteData + byteList
            return

        for b in byteList:
            self.WriteByte(b)




    def ReadUInt8 (self):
        return self.ReadByte()

    def ReadByte(self):
        return self.Unpack('B')

    def WriteUInt8(self, value):
        self.WriteByte(value)

    def WriteByte(self, value):
        self.Append('B', value)




    def ReadInt8(self):
        return self.Unpack('b')

    def WriteInt8(self, value):
        self.Append('b', value)




    def ReadInt16(self):
        return self.Unpack('h')

    def WriteInt16(self, value):
        self.Append('h', value)




    def ReadUInt16(self):
        return self.Unpack('H')

    def WriteUInt16(self, value):
        self.Append('H', value)




    def ReadInt32(self):
        return self.Unpack('i')

    def WriteInt32(self, value):
        self.Append('i', value)




    def ReadUInt32(self):
        return self.Unpack('I')

    def WriteUInt32(self, value):
        self.Append('I', value)




    def ReadInt64(self):
        return self.Unpack('q')

    def WriteInt64(self, value):
        self.Append('q', value)




    def ReadUInt64(self):
        return self.Unpack('Q')

    def WriteUInt64(self, value):
        self.Append('Q', value)




    def ReadDouble(self):
        return self.Unpack('d')

    def WriteDouble(self, value):
        self.Append('d', value)




    def ReadFloat(self):
        return self.Unpack('f')

    def WriteFloat(self, value):
        self.Append('f', value)

