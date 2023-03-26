# Generated by Django 4.1.7 on 2023-03-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_app', '0003_alter_author_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='death_date',
            field=models.DateField(blank=True, help_text='date in "mm/dd/yyyy" format', null=True),
        ),
    ]