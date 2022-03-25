from django.shortcuts import render, get_object_or_404
from .models import Genre,Author,Book
from .forms import GenreForm,AuthorForm,BookForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
	return render(request, 'bookcase/index.html')

def genres(request):
    genreList=Genre.objects.all()
    return render(request,'bookcase/genres.html',{'genreList':genreList})

def authors(request):
    authorList=Author.objects.all()
    return render(request,'bookcase/authors.html',{'authorList':authorList})

def books(request):
    bookList=Book.objects.all()
    return render(request,'bookcase/books.html',{'bookList':bookList})

def bookDetails(request,id):
    book=get_object_or_404(Book,pk=id)
    return render(request,'bookcase/bookdetails.html',{'book':book})

@login_required
def newGenre(request):
	form=GenreForm

	if request.method=='POST':
		form=GenreForm(request.POST)
		if form.is_valid():
			post=form.save(commit=True)
			post.save()
			form=GenreForm
	else:
		form=GenreForm()
	return render(request, 'bookcase/newgenre.html', {'form':form})

@login_required
def newAuthor(request):
	form=AuthorForm

	if request.method=='POST':
		form=AuthorForm(request.POST)
		if form.is_valid():
			post=form.save(commit=True)
			post.save()
			form=AuthorForm
	else:
		form=AuthorForm()
	return render(request, 'bookcase/newauthor.html', {'form':form})

@login_required
def newBook(request):
	form=BookForm

	if request.method=='POST':
		form=BookForm(request.POST)
		if form.is_valid():
			post=form.save(commit=True)
			post.save()
			form=BookForm
	else:
		form=BookForm()
	return render(request, 'bookcase/newbook.html', {'form':form})

def loginmessage(request):
	return render(request,'bookcase/loginmessage.html')

def logoutmessage(request):
	return render(request,'bookcase/logoutmessage.html')