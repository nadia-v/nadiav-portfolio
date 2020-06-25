from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.core.mail import send_mail

from .forms import ContactForm
from .models import Project
from .models import Detail
from .models import Comment

# Create your views here.
def home(request):
    projects = Project.objects
    
    return render(request, 'webpage/home.html', {'projects':projects})

def details(request, project_id):
    
    project_details = get_object_or_404(Project, pk=project_id)
    return render(request, 'webpage/details.html', {'project': project_details})

def resume(request):
    return render(request, 'webpage/resume.html')

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            sender = form.cleaned_data['sender']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
    
            recipients = ['nadia.portfolio.page@gmail.com']
            send_mail(subject + " - " + sender, message, sender, recipients)
            
            return render(request, 'webpage/home.html', {'form': ContactForm})

        else:
            return render(request, 'webpage/home.html', {'form': ContactForm})

    return render(request, 'webpage/home.html', {'form': ContactForm})