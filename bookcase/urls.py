from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('genres/',views.genres, name='genres'),
    path('authors/',views.authors, name='authors'),
    path('books/',views.books, name='books'),
    path('bookDetails/<int:id>', views.bookDetails, name='detail'),
]