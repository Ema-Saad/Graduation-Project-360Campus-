from django.http.response import HttpResponseNotFound, HttpResponse
from .forms import StudentLoginForm
from .models import Person
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from django.urls import reverse
def student_login(request):
    if request.method == "POST":
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("main:student_home")) # Redirect to your home page
            else:
                messages.error(request, "Invalid email/UNIID or password.")
    else:
        form = StudentLoginForm()

    return render(request, "student_login.html", {"form": form})
def student_logout(req):
    logout(req)
    redirect(reverse('main:student_login'))

def student_home(req):
    # If the user is authenticated, render the home page.
    if req.user.is_authenticated:
        return render(req, 'student_home.html', {'user': req.user})
    else:
        return HttpResponseNotFound("Page not found. You need to log in.")   
    
def course_list(req):
    return HttpResponseNotFound()

def course_view(req, course_pk):
    return HttpResponseNotFound()

def classroom_view(req, course_pk):
    return HttpResponseNotFound()

def material_list(req, course_pk):
    return HttpResponseNotFound()

def material_view(req, course_pk, material_pk):
    return HttpResponseNotFound()

