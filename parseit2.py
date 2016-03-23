#!/usr/bin/python
#
#
import xml.etree.ElementTree as ET
tree = ET.parse('config3.xml')
notags = ET.tostring(tree.getroot(),encoding='utf-8',method='text')
print(notags)
