from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import mptt

def index(request):
    return render_to_response('main.html', {}, context_instance=RequestContext(request))