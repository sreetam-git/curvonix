# Generated by Django 5.0.6 on 2024-07-09 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_content', models.TextField()),
                ('main_image', models.ImageField(help_text='Image size : 1500px X 1000px', upload_to='about')),
                ('sub_content', models.TextField()),
                ('sub_image', models.ImageField(help_text='Image size : 1500px X 1000px', upload_to='about')),
                ('home_content', models.TextField()),
                ('image_one', models.ImageField(upload_to='about')),
                ('image_two', models.ImageField(upload_to='about')),
                ('image_three', models.ImageField(upload_to='about')),
                ('image_four', models.ImageField(upload_to='about')),
                ('what_we_do_content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
