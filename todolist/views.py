from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import ToDo
from .forms import ToDoForm

# Create your views here.


def index(request):
    todo_List = ToDo.objects.order_by('id')  # list from DB in admin
    form = ToDoForm()
    context = {'todo_list': todo_List, 'form': form}
    return render(request, 'todolist/index.html', context)


@require_POST
def addToDo(request):
    form = ToDoForm(request.POST)

    if form.is_valid():
        new_todo = ToDo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')


def completeToDo(request, todo_id):
    todo = ToDo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')


def deleteCompleted(request):
    ToDo.objects.filter(complete__exact=True).delete()

    return redirect('index')


def deleteAll(request):
    ToDo.objects.all().delete()

    return redirect('index')
