import re

# the string to search with regex:
test_cases = [
	'maria@abv.bg', # ok
	'ag34_@jfdsfksskkdskda.bg', # not ok
	'ag-34@jfdsfksskkdskd.bg', # not ok
]




# the regex to find if the userEmail contains '@' symbol:
regex = re.compile(r'^(\w{2,10})@([a-z1-9_]{2,20})\.bg', re.I | re.M)


for mail in test_cases:
	match = regex.search(mail)

	if match:
		print(match.groups()[0])
	else:
		print('not ok')
