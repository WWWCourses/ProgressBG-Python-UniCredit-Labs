import xml.etree.ElementTree as ET

tree = ET.parse('./data.xml')
root = tree.getroot()

for elem in root:
		for subelem in elem:
				print(subelem.text)
