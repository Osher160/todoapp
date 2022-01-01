from django.shortcuts import render

from .models import todoapp

# Create your views here.

def index(request):
    todo_items=todoapp.objects.order_by('id')
    context={'todo_items': todo_items}
    return render(request,'todoapp/index.html',context)
    