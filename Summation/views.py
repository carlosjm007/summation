# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

from Summation.models import *
import numpy as np, base64

def suma(request):
	if request.method == 'POST':
		n = int(request.POST["N"])
		matris = np.zeros((n,n,n), dtype=np.uint64)
		s = base64.b64encode(matris)
		id = cubo.objects.create(cubo = s, tamano = n)
		return JsonResponse({"id":id.id}, safe=False)
	return render_to_response('sum.html', context_instance=RequestContext(request))

@csrf_protect
def query(request):
	id = request.POST["id"]
	x1 = int(request.POST["x1"]) - 1
	y1 = int(request.POST["y1"]) - 1
	z1 = int(request.POST["z1"]) - 1
	x2 = int(request.POST["x2"])
	y2 = int(request.POST["y2"])
	z2 = int(request.POST["z2"])
	matris = cubo.objects.get(id=id)
	tam = int(matris.tamano)
	stri = base64.decodestring(matris.cubo)
	mat = np.fromstring(stri, dtype=np.uint64).reshape((tam,tam,tam))
	suma = np.sum(mat[x1:x2,y1:y2,z1:z2])
	return JsonResponse({"respuesta":str(suma), "con":"La respuesta a tu consulta de sumas es"}, safe=False)

@csrf_protect
def update(request):
	id = request.POST["id"]
	x = int(request.POST["x"]) - 1
	y = int(request.POST["y"]) - 1
	z = int(request.POST["z"]) - 1
	matris = cubo.objects.get(id=id)
	stri = base64.decodestring(matris.cubo)
	tam = int(matris.tamano)
	mat = np.fromstring(stri, dtype=np.uint64).reshape((tam,tam,tam))
	mat[x,y,z] = int(request.POST["v"])
	matris.cubo = base64.b64encode(mat)
	matris.save()
	return JsonResponse({"respuesta":"", "con":"Actualización de cubo realizada exitosamente"}, safe=False)