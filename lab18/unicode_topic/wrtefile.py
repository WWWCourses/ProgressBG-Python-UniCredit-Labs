string = "АБВ 123 ИЙК ЩЮЯ"

# open a file handler for writing in binary mode"
with open("encode_to_cp1251.txt", "w+b") as fh:
  bytes_sequence = string.encode(encoding="cp1251")
  fh.write(bytes_sequence)