from django.shortcuts import render, redirect
from rest_framework import viewsets
from . serializers import CourseSerializer
from . models import Course

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


def home(request):

    contex = {
        'key': 'value',
    }
    return render(request, 'home.html', contex)