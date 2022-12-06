from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def calc(request):
    a=int(request.GET['n1'])
    b=int(request.GET['n2'])
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return render(request,'operation.html',{'add':add,'sub':sub,'mul':mul,'div':div})
