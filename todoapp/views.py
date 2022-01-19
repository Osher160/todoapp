from django.shortcuts import render,redirect

from .models import todoapp

from .forms import TodoListForm

from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    todo_items=todoapp.objects.order_by('id')
    form=TodoListForm()
    context={'todo_items': todo_items, 'form': form}
    return render(request,'todoapp/index.html',context)

@require_POST
def addTodoItem(request):
    form=TodoListForm(request.POST)

    if form.is_valid():
        new_todo= todoapp(text=request.POST['text'])
        new_todo.save()

    return redirect("index")
    
def completedTodo(request, todo_id) :
    todo = todoapp.objects.get(pk=todo_id)
    todo.complited=True
    todo.save()

    return redirect('index')

def deletecompleted(request):
    todoapp.objects.filter(complited__exact=True).delete()

    return redirect('index')

def deleteall(request):
    todoapp.objects.all().delete()

    return redirect('index')