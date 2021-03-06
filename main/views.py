from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Books
from django.views.generic import DetailView

def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html', {"todo_list": todo_list})

def second(request):
    book = Books.objects.all()
    return render(request, 'books.html', {"book": book})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text = text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id = id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id = id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id = id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def done_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_done = True
    todo.save()
    return redirect(test)

def undone_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_done = False
    todo.save()
    return redirect(test)

# books function

def delete_books(request, id):
    books = Books.objects.get(id = id)
    books.delete()
    return redirect(second)

def mark_books(request, id):
    books = Books.objects.get(id = id)
    books.is_favorite = True
    books.save()
    return redirect(second)

def unmark_books(request, id):
    books = Books.objects.get(id = id)
    books.is_favorite = False
    books.save()
    return redirect(second)


class booksinfo(DetailView):
    model = Books
    tamplate_name ='books_datail.html'
    context_object_name = 'info'
