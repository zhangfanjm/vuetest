from django.shortcuts import render
from django.http import JsonResponse
from .models import Stu
from rest_framework import serializers
from django.core import serializers

# Create your views here.
def test(request):
	return JsonResponse({"status": 0, "message":"This is Django Message hello"})

def ret_user(request):
	if request.method == "GET":
		#db = Stu.objects.all()
		#db = [i.name for i in db]
		user_list = Stu.objects.all()
		json = serializers.serialize("json", user_list)
		print(json)
		return JsonResponse({"status": 0, "data": json})
	else :
		return JsonResponse({"status": 1, "message":"you need GET method"})