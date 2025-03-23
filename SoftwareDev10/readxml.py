import xml.etree.ElementTree as ET
tree = ET.parse('SoftwareDev10/train.xml')
root = tree.getroot()

print(ET.tostring(root))

company = root.get('com')

print("Company name ={val} ".format(val))
