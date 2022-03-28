s = 'юя'

byte_str = s.encode('utf-8')
print(byte_str)
print(type(byte_str))
print(len(byte_str))

s2 = byte_str.decode('utf-8')
print(s2)
print(type(s2))
print(len(s2))


