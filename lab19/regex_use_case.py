import re

test_case = """
a    a 			b
dsfld sldslds
"""

rx = re.compile(r'\s+')

cleared = rx.sub('',test_case)

print(cleared)