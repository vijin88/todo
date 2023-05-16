from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task
from .form import TodoForm
# Create your views here.
def index(request):
    if request.POST:
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        task1=Task(name=name,priority=priority,date=date)
        task1.save()
    detail=Task.objects.all()
    return render(request,'home.html',{'detail':detail})

def delete(request,taskid):
    if request.POST:
        task1=Task.objects.get(id=taskid)
        task1.delete()
        return redirect('/')
    return render(request,'delete.html')

def edit(request,id):
    task1=Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=task1)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task1':task1})