import re

html = '''
<h1>Book Title</h1>
<p>dome text<
/p>
<a href="https://jkjfkds.ocm" title="sfjkdsjdsk">some link</a>
'''

# rx = re.compile(r'(?s)<.+?>')
rx = re.compile(r'<[^>]+>')
stripped = rx.sub('',html)

print(stripped)

