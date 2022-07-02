
# Create your views here.
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import *
  
def index(request):
    return render(request,'mentor/index.html')

def mentor_img(request):
  
    if request.method == 'POST':
        form = MentorForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MentorForm()
    return render(request, 'mentor/admin.html', {'form' : form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')




def display_images(request):
  
    if request.method == 'GET':
  
        # getting all the objects of hotel.
        Mentors = mentor.objects.all() 
        return render(request, 'mentor/display_img.html', {'mentor_images' : Mentors})