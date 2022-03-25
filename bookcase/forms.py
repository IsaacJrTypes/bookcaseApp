from django import forms
from .models import Genre,Author,Book

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'