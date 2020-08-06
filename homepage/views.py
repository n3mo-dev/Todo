from django.shortcuts import render
from homepage.models import Todo 

# Create your views here.
def mainpage(request):
    return render(request, 'mainpage.html')

def todo(request):
    item = Todo.objects.all()
    dict = { 'item' : item }
    return render(request, 'todo.html', dict)