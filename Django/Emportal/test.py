from xml.etree import ElementTree

f = r"D:\Technical\Practise\Django\emportal\serverips\data\servers.xml"

root = ElementTree.parse(f).getroot()

matchEle = root.findtext('Kevin')

# outputList = []

# root = ElementTree.parse(f).getroot()
# allEle = root.findall('Server')
# if allEle is not None:
# 	for e in allEle:
# 		output = {}
# 		for i in list(e):
# 			if i.text is not None:
# 				output[i.tag] = i.text
# 			else:
# 				output[i.tag] = ''
# 		outputList.append(output)

# print outputList
