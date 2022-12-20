from django.shortcuts import render
from .models import Place
from .serializers import PlaceSerializer
from rest_framework.response import Response

from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.http import HttpResponse




class PlaceViewSet(viewsets.ViewSet):
    def list(self,request):
        place=Place.objects.all()
        serializer= PlaceSerializer(place,many=True)
        return Response(serializer.data)
    

    def create(self,request):
        serializer=PlaceSerializer(data=request.data)
         
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        

    def retrive(self,request,pk=None):
        queryset=Place.objects.all()
        place=get_object_or_404(queryset,pk=pk)
        serializer=PlaceSerializer(place) 
        return Response(serializer.data)

    def update(self,request,pk=None):
        place=Place.objects.get(pk=pk)
        serializer=PlaceSerializer(place,data=request.data) 

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


    def progress(request, pk):
        to = get_object_or_404(Todo, pk=pk)
        to.update_status()
            
           

        