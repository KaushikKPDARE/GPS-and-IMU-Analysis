"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class example_t(object):
    __slots__ = ["time", "latitude", "longitude", "altitude"]

    def __init__(self):
        self.time = ""
        self.latitude = ""
        self.longitude = ""
        self.altitude = ""

    def encode(self):
        buf = BytesIO()
        buf.write(example_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        __time_encoded = self.time.encode('utf-8')
        buf.write(struct.pack('>I', len(__time_encoded)+1))
        buf.write(__time_encoded)
        buf.write(b"\0")
        __latitude_encoded = self.latitude.encode('utf-8')
        buf.write(struct.pack('>I', len(__latitude_encoded)+1))
        buf.write(__latitude_encoded)
        buf.write(b"\0")
        __longitude_encoded = self.longitude.encode('utf-8')
        buf.write(struct.pack('>I', len(__longitude_encoded)+1))
        buf.write(__longitude_encoded)
        buf.write(b"\0")
        __altitude_encoded = self.altitude.encode('utf-8')
        buf.write(struct.pack('>I', len(__altitude_encoded)+1))
        buf.write(__altitude_encoded)
        buf.write(b"\0")

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != example_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return example_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = example_t()
        __time_len = struct.unpack('>I', buf.read(4))[0]
        self.time = buf.read(__time_len)[:-1].decode('utf-8', 'replace')
        __latitude_len = struct.unpack('>I', buf.read(4))[0]
        self.latitude = buf.read(__latitude_len)[:-1].decode('utf-8', 'replace')
        __longitude_len = struct.unpack('>I', buf.read(4))[0]
        self.longitude = buf.read(__longitude_len)[:-1].decode('utf-8', 'replace')
        __altitude_len = struct.unpack('>I', buf.read(4))[0]
        self.altitude = buf.read(__altitude_len)[:-1].decode('utf-8', 'replace')
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if example_t in parents: return 0
        tmphash = (0xb134288271185d99) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if example_t._packed_fingerprint is None:
            example_t._packed_fingerprint = struct.pack(">Q", example_t._get_hash_recursive([]))
        return example_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

