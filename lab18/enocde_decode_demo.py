# symbol = '😼'
# print(symbol)
# print(ord(symbol))

# # A => 65
# print(ord('A'))
# print(chr(128572))


# print('\uD83D')

# -------------------------------- decode demo ------------------------------- #
# decode
# with open('./data.txt','r', encoding='cp1251') as f:
# 	content = f.read()
# 	print(content)


# new_content = content.upper()
# print(new_content)

# encode:
# with open('./new_data.txt', 'w', encoding='cp1251') as f:
# 	f.write(new_content)

# some_str = 'някакъв текст'
# some_str_bytes = some_str.encode(encoding='cp1251')
# print(some_str_bytes)

# with open('./new_data.txt', 'wb') as f:
# 	f.write(some_str_bytes)

# some_str = '😼'
# some_str_bytes = some_str.encode(encoding='utf_8')

# print(len(some_str))
# print(len(some_str_bytes))

tmp = b'\xed\xff\xea\xe0\xea\xfa\xe2 \xf2\xe5\xea\xf1\xf2'

str1 = tmp.decode(encoding='cp1251')
print(str1)


