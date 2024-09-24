from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import CarsSerializer
from .models import Cars

@api_view(['GET', 'POST'])
def cars_list(request):
    
    if request.method == 'GET':
        cars = Cars.objects.all()
        serializer = CarsSerializer(cars, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CarsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['PUT', 'DELETE', 'GET'])
def cars_details(request, pk):
    
    cars = get_object_or_404(Cars, pk=pk)
    
    if request.method == 'GET':
        serializer = CarsSerializer(cars)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        serializer = CarsSerializer(cars, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        cars.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def cars_by_make(request, make):
    
    if request.method == 'GET':
        cars = Cars.objects.all()
        cars_make = cars.filter(make=make)
        
        if cars_make:
            serializer = CarsSerializer(cars_make, many=True)
            return Response(serializer.data)
        else: return Response("No cars of that make.")