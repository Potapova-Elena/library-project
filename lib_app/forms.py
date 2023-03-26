from django import forms
from .models import Author, Book
from django.core.exceptions import ValidationError

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['Name', 'Surname', 'birth_date', 'death_date']
        labels = {'Name': 'First name', 'Surname': 'Last name', 'birth_date': 'Birth date', 'death_date': 'Death date'}

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['Title', 'Author', 'Summary', 'Publish_date']
        labels = {'Title': 'Title', 'Author': 'Author', 'Summary': 'Summary', 'Publish_date': 'Publish date'}
        # widgets = {'note_name': forms.TextInput(attrs={'cols': 80, 'rows': 1})}

