import re

mails =[
	'maria@abv.bg', # ok,
	'@abv.bg', # not,
	'ala123@abv.bg', # ok,
	'ala123@abvbg', # not
	'ala_123@abv.bg', # ok,
	'ala_123@abv.bg983485$#%$#%$#%43', # not,
	'ala_123@gmail.bg', # ok,
	'---ala_123@abv.bg' # not,
]

rx = re.compile(r'^\w+@[a-z]{1,5}\.bg$')

for mail in mails:
	m = rx.search(mail)
	if m:
		print(f'{mail} => ok')
	else:
		print(f'{mail} => not')
