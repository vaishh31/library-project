# Generated by Django 4.0.4 on 2022-06-14 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='book_author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='book_name',
        ),
    ]