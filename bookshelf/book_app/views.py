import json
from django.http import HttpResponse
from django.shortcuts import render
# IMPORT MODELS
from .models import Book, Genre

# CSRF TOKEN
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def list_genres(request):
    genres = Genre.objects.all()
    print(genres)
    data = {"genres" : genres}
    return render(request, 'book_app/list_genres.html', data)

def list_books(request, genre_id):
    # return HttpResponse("<h1> LIST BOOKS </h1>")
    genre_books = Book.objects.all().filter(genre_id = genre_id)
    genre_name = Genre.objects.all().get(id = genre_id)
    data = {"books": genre_books, "genre": genre_name}
    return render(request, 'book_app/list_books.html', data)

def book_info(request, genre_id, book_id):
    book = Book.objects.all().get(id = book_id)
    data = {"book" : book}
    return render(request, 'book_app/book_info.html', data)

# Post vs Get
@csrf_exempt
def add_book(request, genre_id):
    if request.method == "POST":
        body = json.loads(request.body)
        newBook = Book(title = body["title"], author = body["author"], description = body["description"], genre_id = genre_id)
        newBook.save()
    # default get request
    return render(request, "book_app/add_book.html")

@csrf_exempt
def edit_book(request, genre_id, book_id):
    if request.method == "POST":
        body = json.loads(request.body)

        # get the book we want to change
        book = Book.objects.all().get(id = book_id)

        # Edit the information
        book.title = body['title']
        book.author = body['author']
        book.description = body['description']

        #save the information
        book.save()
    data = {"book": Book.objects.all().get(id = book_id)}
    return render(request, "book_app/edit_book.html", data)