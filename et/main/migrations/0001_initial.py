# Generated by Django 3.1.3 on 2020-11-10 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Название')),
                ('name', models.CharField(max_length=50, verbose_name='Имя поставщика')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('category', models.CharField(choices=[('Мясная продукция', 'Мясная продукция'), ('Кисломолочная продукция', 'Кисломолочная продукция'), ('Овощи и фрукты', 'Овощи и фрукты')], max_length=30, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('time', models.DateField(auto_now=True, max_length=5, verbose_name='Время')),
                ('place', models.CharField(default='Казахстан', max_length=65, verbose_name='Местоположение')),
                ('img', models.ImageField(upload_to='img/')),
            ],
        ),
    ]
