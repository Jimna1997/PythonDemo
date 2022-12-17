from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie

def home(request):
    movie_list=Movie.objects.all()
    return render(request,'home.html',{'movie_list': movie_list})

def details(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movie': movie})
    # return HttpResponse("This is movie no %s"%movie_id)

def addmovie(request):
    if request.method=='POST':
        name=request.POST['name']
        desc=request.POST['desc']
        year=request.POST['year']
        img=request.FILES['img']
        movie=Movie(name=name,desc=desc,img=img,year=year)
        movie.save()
        return redirect('/')
    else:
        return render(request,'addmovie.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    else:
        return render(request,'delete.html')