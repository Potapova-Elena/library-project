from django.test import TestCase

# Create your tests here.

from .forms import AuthorForm


class AuthorFormTest(TestCase):

    def test_author_form_name_field_label(self):
        """Test renewal_date label is 'renewal date'."""
        form = AuthorForm()
        self.assertTrue(
            form.fields['Name'].label == 'First name')

    def test_author_form_surname_field_label(self):
        """Test renewal_date label is 'renewal date'."""
        form = AuthorForm()
        self.assertTrue(
            form.fields['Surname'].label == 'Last name')

    def test_author_form_birth_date_field_label(self):
        """Test renewal_date label is 'renewal date'."""
        form = AuthorForm()
        self.assertTrue(
            form.fields['birth_date'].label == 'Birth date')

    def test_author_form_death_date_field_label(self):
        """Test renewal_date label is 'renewal date'."""
        form = AuthorForm()
        self.assertTrue(
            form.fields['death_date'].label == 'Death date')