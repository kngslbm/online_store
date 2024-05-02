from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Category
from .serializers import CategoreySerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all categoreys.
    """

    queryset = Category.objects.all()

    def list(self, request):
        serializer = CategoreySerializer(self.queryset, many=True)
        return Response(serializer.data)
