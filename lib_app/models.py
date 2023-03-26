from django.db import models

# Create your models here.

class Author (models.Model):
    Name = models.CharField(max_length=50, null=False)
    Surname = models.CharField(max_length=100, null=False)
    birth_date = models.DateField(null=False, help_text='date in "mm/dd/yyyy" format')
    death_date = models.DateField(null=True, blank=True, help_text='date in "mm/dd/yyyy" format')

    class Meta:
        unique_together = ('Name', 'Surname')

    def __str__(self):
        return f'{self.Name} {self.Surname}'


class Book(models.Model):
    Title = models.CharField(unique=True, max_length=150, null=False)
    Author = models.ManyToManyField(Author, help_text="Select an author for this book")
    Summary = models.TextField(max_length=1000, help_text="Brief description for this book", null=False)
    Publish_date = models.DateField(help_text="First publication date. Date in 'mm/dd/yyyy' format", null=False)

    def __str__(self):
        return f'{self.Title}. {self.Summary[:50]}'
