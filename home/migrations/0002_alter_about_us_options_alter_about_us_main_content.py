# Generated by Django 5.0.6 on 2024-07-09 18:50

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about_us',
            options={'verbose_name_plural': 'About us'},
        ),
        migrations.AlterField(
            model_name='about_us',
            name='main_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
