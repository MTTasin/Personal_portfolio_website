from django.shortcuts import render
from .models import portfolio_model, contact as c

# Create your views here.

def index(request):
    projects = portfolio_model.objects.all()
    context = {'projects': projects}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    projects = portfolio_model.objects.all()
    context = {'projects': projects}
    return render(request, 'portfolio.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        ls = c(name=name, email=email, subject=subject, message=message)
        ls.save()
        return render(request, 'contact_success.html')
    else:
        return render(request, 'contact.html')

    return render(request, 'contact.html')

def project_details(request, id):
    project = portfolio_model.objects.get(id=id)
    technology = portfolio_model.objects.get(id=id).technology_used.all()
    context = {
        'project': project,
        'technology': technology
    }
    return render(request, 'single-project.html', context)