from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse

#----- Django Auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer, UserSerializer, AuthSerializer

from .models import Booking
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		'Create User': '/create-user/',
		'Auth User': '/auth-user/'
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Booking.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Booking.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
	serializer = UserSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return HttpResponseRedirect('../')


@api_view(['POST'])
def authUser(request):
	serializer = AuthSerializer(data=request.data)
	
	serializer.is_valid(raise_exception=True)
	
	#username = serializer.validated_data['username']
	#password = serializer.validated_data['password']
 
	auth = authenticate(serializer)
 
	if auth is not None:
		login(request, auth)
		return Response(data=serializer.data)
	else: return HttpResponse('Falha na autenticação') 

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Booking.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Booking.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')



