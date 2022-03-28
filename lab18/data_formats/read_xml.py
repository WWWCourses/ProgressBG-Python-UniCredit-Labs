import xml.etree.ElementTree as ET

root = ET.parse('./demo.xml').getroot()

for item in root:
	# print(item)
	for fruit in item:
		print(fruit.attrib, fruit.text)