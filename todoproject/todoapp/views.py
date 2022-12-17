from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import TodoForm
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

#Class generic view
class TaskListView(ListView):
    model = Task
    template_name='home.html'
    context_object_name = 'task1'

class TaskDetailView(DetailView):
    model = Task
    template_name='details.html'
    context_object_name = 't'

class TaskUpdateView(UpdateView):
    model = Task
    template_name='edit1.html'
    # context_object_name = 't'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('todoapp:cbvdetails',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name='delete.html'
    success_url = reverse_lazy('todoapp:cbvhome')

# Create your views here.
def add(request):
    task1=Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        task = Task(name=name, priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})

# def details(request):
#     task=Task.objects.all()
#     return render(request,'details.html',{'task':task})

def delete(request,taskid):
    if request.method=='POST':
        task=Task.objects.get(id=taskid)
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,taskid):
    task=Task.objects.get(id=taskid)
    form=TodoForm(request.POST or None, request.FILES, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task})
