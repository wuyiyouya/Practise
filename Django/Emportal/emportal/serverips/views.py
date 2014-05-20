from django.http import HttpResponse
from django.shortcuts import render_to_response
from serverips.sforms import searchServerForm
from django.template import RequestContext
from emportal.views import readXML
import os

#serverXML = os.path.join(os.path.dirname(__file__), '../serverips/data/servers.xml')
serverXML = r'D:\Technical\Practise\Django\emportal\serverips\data\servers.xml'

def servers(request):
	# if request.method == 'POST':
	# 	form = ServerForm(request.POST)
	# 	if form.is_valid():
	# 		return HttpResponse("thanks")
	# else:
	# 	form = ServerForm()
	# return render_to_response('html/servers.html', {'form':form}, context_instance=RequestContext(request))
	 
	form = searchServerForm()
	return render_to_response('html/servers.html', {'form':form, 'serverlist':readXML('Server',serverXML)}, context_instance=RequestContext(request))