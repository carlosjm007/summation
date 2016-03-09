from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

from Summation.models import *
import numpy, urllib, json

def suma(request):
	return render_to_response('sum.html',context_instance=RequestContext(request))