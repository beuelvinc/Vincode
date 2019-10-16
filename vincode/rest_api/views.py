from django.shortcuts import render
from rest_framework import viewsets
from .serializers import VincodeSerializer, ImageSerializer
from mainApp.models import Vincode,Image
from rest_framework import serializers
class VincodeViewSet(viewsets.ModelViewSet):
	queryset = Vincode.objects.all()
	serializer_class = VincodeSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer