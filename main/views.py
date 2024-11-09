from django.shortcuts import render
from .models import About, Resume, Skill, Project, Contact

def home(request):
    about = About.objects.first()
    resume = Resume.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    contact = Contact.objects.first()
    context = {
        'about': about,
        'resume': resume,
        'skills': skills,
        'projects': projects,
        'contact': contact
    }
    return render(request, 'main/home.html', context)

def about(request):
    about = About.objects.first()
    return render(request, 'main/about.html', {'about': about})

def resume(request):
    resume = Resume.objects.all()
    return render(request, 'main/resume.html', {'resume': resume})

def skills(request):
    skills = Skill.objects.all()
    return render(request, 'main/skills.html', {'skills': skills})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})

def contact(request):
    contact = Contact.objects.first()
    return render(request, 'main/contact.html', {'contact': contact})
