import re

# the string to search with regex:
# valid bg tel is +359DDDDDDDD
test_strings = [
'maria : +36212345678',
'asen: +35912345678',
'stoyan: +359123456789',
]

# rx = re.compile(r'[a-zA-Z0-9_]+@')
rx = re.compile(r'^([a-z]+\s*):\s*(\+359\d{8})$')


for test_str in test_strings:
	m = rx.search(test_str)
	if m:
		print(f'{test_str} => ok')
		print(m.groups()[1])
	else:
		print(f'{test_str} => not')




# /a*/ => '', 'a', 'aa', 'aaa', ...,'aaaaaaaa....a'


# /t{2}/ => 'tt'
# /t{2,4}/ => 'tt', 'ttt', 'tttt'

# /a.*a/ => 'afkdsjfkdslkdsglkdsjgdsklglkjgka', 'aaa'

# /a.*?a/  =>aa


# /[abc]/ => 'a','b', 'c'

# /[^abc]/ => 'd', '-',