from django.test import TestCase
from .models import Genre,Author,Book
from .forms import GenreForm,AuthorForm,BookForm
# Create your tests here.
class GenreTest(TestCase):
    def setup(self):
        genre=Genre(genreName='genre test', genreDescription='desc test')
        return genre
    
    def test_string(self):
        genre = self.setup()
        self.assertEqual(str(genre),genre.genreName)

    def test_table(self):
        self.assertEqual(str(Genre._meta.db_table),'genrename')

class AuthorTest(TestCase):
    def setup(self):
        genre=Genre(genreName='genre test')
        author=Author(authorName='author test', authorNotes='author test',genreName=genre)
        return author

    def test_string(self):
        author = self.setup()
        self.assertEqual(str(author),author.authorName)

    def test_table(self):
        self.assertEqual(str(Author._meta.db_table),'authorname') 

class BookTest(TestCase):
    def setup(self):
        genre=Genre(genreName='genre test')
        author=Author(authorName='author test')
        book=Book(bookTitle='book',genreName=genre, authorName=author,pages=21,startDate='2022-3-6',endDate='2022-3-7',bookNotes='book notes')
        return book

    def test_string(self):
        book = self.setup()
        self.assertEqual(str(book),book.bookTitle)

    def test_table(self):
        self.assertEqual(str(Book._meta.db_table),'book')

class NewGenreForm(TestCase):
    def test_genreForm(self):
        data={
            'genreName':'testing',
            'genreDescription':'test desc'
            }
        form=GenreForm(data)
        self.assertTrue(form.is_valid)

class NewAuthorForm(TestCase):
    def test_authorForm(self):
        data={
            'AuthorName':'testing',
            'authorNotes':'test notes',
            'genreName': 'test'
            }
        form=AuthorForm(data)
        self.assertTrue(form.is_valid)

class NewBookForm(TestCase):
    def test_bookForm(self):
        data={
            'bookTitle':'testing',
            'genreName':'test notes',
            'authorName': 'test',
            'pages': '200',
            'startDate': '01/01/2022',
            'endDate': '01/02/2022',
            'bookNotes': 'test'
            }
        form=BookForm(data)
        self.assertTrue(form.is_valid)
