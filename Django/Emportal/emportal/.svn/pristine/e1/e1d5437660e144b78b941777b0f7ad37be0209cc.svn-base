from django.http import HttpResponse
from django.shortcuts import render_to_response
from xml.etree import ElementTree

def hello(request):
	return render_to_response('html/emportal.html')

def readXML(typ, f):

	outputList = []

	root = ElementTree.parse(f).getroot()
	allEle = root.findall(typ)
	if allEle is not None:
		for e in allEle:
			output = {}
			for i in list(e):
				if i.text is not None:
					output[i.tag] = i.text
				else:
					output[i.tag] = ''
			outputList.append(output)

	return outputList

def searchXML(typ, f):
	pass
