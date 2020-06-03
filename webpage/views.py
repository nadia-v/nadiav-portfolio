from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.template.loader import get_template

from .models import Project
from .models import Detail
from .models import Comment

# Create your views here.
def home(request):
    projects = Project.objects
    return render(request, 'webpage/home.html', {'projects':projects})