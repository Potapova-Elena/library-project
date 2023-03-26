from django.test import TestCase

# Create your tests here.

from .models import Author


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(Name='Mark', Surname='Twain', birth_date='1835-11-30', death_date='1910-04-21')

    def test_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('Name').verbose_name
        self.assertEquals(field_label, 'Name')

    def test_surname_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('Surname').verbose_name
        self.assertEquals(field_label, 'Surname')

    def test_birth_date_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('birth_date').verbose_name
        self.assertEquals(field_label, 'birth date')

    def test_death_date_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('death_date').verbose_name
        self.assertEquals(field_label, 'death date')

