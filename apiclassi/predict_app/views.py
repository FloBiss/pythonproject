from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Subject
from .serializers import SubjectSerializer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
	return HttpResponse("You are on the main page: isn't it beautiful?")

@csrf_exempt
def i_want_a_list(request):
	if request.method == "GET":
		subjects = Subject.objects.all()
		serializer = SubjectSerializer(subjects, many=True)
		return JsonResponse(serializer.data, safe=False)
	else:
		return HttpResponse(status = 404)
	
@csrf_exempt
def subject_detail(request, subject_id):
	try:
		subject = Subject.objects.get(pk=subject_id)
	except Subject.DoesNotExist:
		return HttpResponse(str(subject_id), status = 404)
	if request.method == "GET":
		serializer = SubjectSerializer(subject)
		return JsonResponse(serializer.data)
	else:
		return HttpResponse(status = 404)
	

def predict_act(data):
	from sklearn.externals import joblib
	colonnes = 	["AGE", "SPORT", "WEIGHT", "HEIGHT", "label", "zchest", "zwrist", "temp"]
	path_to_model = "./rfclassi.sav"
	data = [data[colonne] for colonne in colonnes]
	model = joblib.load(path_to_model)
	act = model.predict(data)
	return act

@csrf_exempt
def predict(request):
	if request.method == "GET":
		return JsonResponse(serializer.errors, status = 400)
		
	elif request.method == "POST":
		data = JSONParser().parse(request)
		serializer = SubjectSerializer(data=data)
		if serializer.is_valid():
			data["activity"] = predict_act(data)
			serializer = SubjectSerializer(data=data)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse(serializer.data, status=201)
	return JsonResponse(serializer.errors, status = 404)