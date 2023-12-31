# Generated by Django 4.2.8 on 2023-12-06 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('cover', models.ImageField(default='default.jpg', upload_to='')),
                ('title', models.CharField(default='unknown', max_length=200)),
                ('author_name', models.CharField(default='unknown', max_length=200)),
                ('author_img', models.ImageField(default='default.jpg', upload_to='')),
                ('time', models.DateTimeField()),
                ('desc_par1', models.TextField()),
                ('desc_par2', models.TextField()),
                ('desc_par3', models.TextField()),
                ('details_title', models.CharField(default='unknown', max_length=200)),
                ('details_quote', models.CharField(default='unknown', max_length=200)),
                ('details_par1', models.TextField()),
                ('details_par2', models.TextField()),
                ('details_par3', models.TextField()),
            ],
        ),
    ]
