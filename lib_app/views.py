from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm
# from django.contrib.auth.decorators import login_required
# from django.http import Http404
# from django.core.exceptions import ValidationError, ObjectDoesNotExist


# Create your views here.

def index(request):
    """The home page for library"""
    return render(request, 'lib_app/index.html')

def view_book(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {'book': book}
    return render(request, 'lib_app/view_book.html', context)


def books(request):
    """Shows book list"""
    books = Book.objects.order_by('Title')
    context = {'books': books}
    return render(request, 'lib_app/books.html', context)


def add_book(request):
    if request.method != 'POST':
        form = BookForm()
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lib_app:books')
    context = {'form': form}
    return render(request, 'lib_app/add_book.html', context)


def update_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method != 'POST':
        form = BookForm(instance=book)
    else:
        form = BookForm(request.POST, instance=book)
    if form.is_valid():
        form.save()
        return redirect('lib_app:books')
    context = {'book': book, 'form': form}
    return render(request, 'lib_app/update_book.html', context)


def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
    return redirect('lib_app:books')


# def find_book(request):
#     """"""
#     pass

def authors(request):
    """Shows author list"""
    authors = Author.objects.order_by('Name', 'Surname')
    context = {'authors': authors}
    return render(request, 'lib_app/authors.html', context)

def view_author(request, author_id):
    author = Author.objects.get(id=author_id)
    books = Book.objects.filter(Author=author_id)
    context = {'author': author, 'books': books}
    return render(request, 'lib_app/view_author.html', context)


def add_author(request):
    if request.method != 'POST':
        form = AuthorForm()
    else:
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lib_app:authors')
    context = {'form': form}
    return render(request, 'lib_app/add_author.html', context)


def update_author(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method != 'POST':
        form = AuthorForm(instance=author)
    else:
        form = AuthorForm(request.POST, instance=author)
    if form.is_valid():
        form.save()
        return redirect('lib_app:authors')
    context = {'author': author, 'form': form}
    return render(request, 'lib_app/update_author.html', context)


def delete_author(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method == 'POST':
        author.delete()
    #     DB error may be occurred
    return redirect('lib_app:authors')


# def find_author(request):
#     """"""
#     pass
