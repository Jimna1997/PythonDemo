from django.shortcuts import render
from . models import Place
from . models import Team

def index(request):
    # p1= Place()
    # p1.name='Kerala'
    # p1.des='Gods own country'
    # p1.img='destination_1.jpg'
    # p2 = Place()
    # p2.name = 'Mumbai'
    # p2.img = 'destination_2.jpg'
    # p2.des = 'City that not sleeps'
    # p=[p1,p2]
    p=Place.objects.all()
    t=Team.objects.all()
    return render(request,'index.html',{'p':p,'t':t})

