from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # Shows all your books in a genre
    path('', views.list_genres, name = "list_genres"),
    path('genres/', views.list_genres, name = "list_genres"),
    path('<int:genre_id>/', views.list_books, name = "list_books"),
    path('<int:genre_id>/books/<int:book_id>/', views.book_info, name = "book_info"),
    path('<int:genre_id>/books/<int:book_id>/edit/', views.edit_book, name = "edit_book"),
    path('<int:genre_id>/books/new/', views.add_book, name = "add_book")
]