from django.shortcuts import render
from .models import Genre,Author,Book

# Create your views here.
def index(request):
	return render(request, 'bookcase/index.html')

def genres(request):
    genreList=Genre.objects.all()
    return render(request,'bookcase/genres.html',{'genreList':genreList})

def authors(request):
    authorList=Author.objects.all()
    return render(request,'bookcase/authors.html',{'authorList':authorList})