# Generated by Django 4.1.7 on 2023-03-25 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Surname', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('death_date', models.DateField(null=True)),
            ],
            options={
                'unique_together': {('Name', 'Surname')},
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=150, unique=True)),
                ('Summary', models.TextField(help_text='Brief description for this book', max_length=1000)),
                ('Publish_date', models.DateField(help_text='First publication date')),
                ('Author', models.ManyToManyField(help_text='Select an author for this book', to='lib_app.author')),
            ],
        ),
    ]
