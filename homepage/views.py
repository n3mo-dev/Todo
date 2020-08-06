from django.shortcuts import render, HttpResponseRedirect
from homepage.models import Todo 

# Create your views here.
def mainpage(request):
    return render(request, 'mainpage.html')

def todo(request):
    item = Todo.objects.all()
    dict = { 'item' : item }
    return render(request, 'todo.html', dict)

def addtodo(request):
    item = Todo(Data = request.POST['data'])
    item.save()
    return HttpResponseRedirect('/todo/')

def deletetodo(request, itemid):
    item  = Todo.objects.get(id=itemid)
    item.delete()
    return HttpResponseRedirect('/todo/') 