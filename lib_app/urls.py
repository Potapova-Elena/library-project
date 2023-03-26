"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from . import views


app_name = 'lib_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('add_book/', views.add_book, name='add_book'),
    path('books/', views.books, name='books'),
    path('view_book/<int:book_id>/', views.view_book, name='view_book'),
    path('update_book/<int:book_id>/', views.update_book, name='update_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('authors/', views.authors, name='authors'),
    path('view_author/<int:author_id>/', views.view_author, name='view_author'),
    path('add_author/', views.add_author, name='add_author'),
    path('update_author/<int:author_id>/', views.update_author, name='update_author'),
    path('delete_author/<int:author_id>/', views.delete_author, name='delete_author'),
]
