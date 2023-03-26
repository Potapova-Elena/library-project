from django.test import TestCase

# Create your tests here.

from .models import Author
from django.urls import reverse


class AuthorViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 4 authors for tests
        for author_num in range(1, 5):
            Author.objects.create(Name='Christian %s' % author_num,
                                  Surname='Surname %s' % author_num,
                                  birth_date='1990-01-%s' % author_num,
                                  death_date='2000-01-%s' % author_num)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/authors/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('authors', urlconf='lib_app.urls', current_app='lib_app'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('authors', urlconf='lib_app.urls', current_app='lib_app'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'lib_app/authors.html')

    def test_four_authors_are_present(self):
        resp = self.client.get(reverse('authors', urlconf='lib_app.urls', current_app='lib_app'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context['authors']) == 4)

