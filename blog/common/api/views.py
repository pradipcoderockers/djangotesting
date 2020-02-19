from django.shortcuts import render
from ..models import Category
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    
        
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
     
# Create your views here.
