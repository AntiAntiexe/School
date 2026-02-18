import xml.etree.ElementTree as ET

tree = ET.parse('/Users/anton/Programming/pythonProjects/School/softwareDev34/Unit3/AOS1/fileXML.xml')
root = tree.getroot()

for student in root.findall('student'):
    name = student.find('name').text
    age = student.find('age').text
    grade = student.find('grade').text
    print(f"Name: {name}, Age: {age}, Grade: {grade}")
    