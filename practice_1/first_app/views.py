from django.shortcuts import render,redirect
from .forms import contactForm
from . import models



def index(request):
    Student = models.Student.objects.all()  
    return render(request, "first_app/index.html" , {"data": Student})

def delete_student(request, roll):
    student = models.Student.objects.get( pk = roll)
    student.delete()
    return redirect("home")

def model_form(request):
    mymodel = models.MyModel.objects.all()
    return render(request, "first_app/model_form.html" , {"mymodel": mymodel})

def about(request):
    if request.method == "POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        return render(request, "first_app/about.html", {"name": name, "email": email})
    else:
        return render(request, "first_app/about.html")


def form(request):
    return render(request, "first_app/form.html")


def django_form(request):
    # if request.method == 'POST':
    form = contactForm()
    if form.is_valid():
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        text = form.cleaned_data["text"]
        print(name, email, text)
        return render(request, "first_app/django_form.html", {"form": form})
    else:
        form = contactForm()
        return render(request, "first_app/django_form.html", {"form": form})
