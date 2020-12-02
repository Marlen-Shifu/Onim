from django.db import models
from django.contrib.auth.models import User

class Offer(models.Model):
	
	title = models.CharField(max_length= 25, verbose_name = 'Название')

	name = models.ForeignKey(User, on_delete=models.CASCADE)

	
	
	price = models.IntegerField(verbose_name = 'Цена')

	choice_category = [ 
						('Мясная продукция', 'Мясная продукция'),
						('Кисломолочная продукция', 'Кисломолочная продукция'),
						('Овощи и фрукты', 'Овощи и фрукты'),
					  ]
	category = models.CharField(max_length = 30, choices = choice_category, verbose_name = 'Категория')

	description = models.TextField(verbose_name = 'Описание')
	
	time = models.DateField(max_length = 5, verbose_name = 'Время', auto_now = True)
	
	place = models.CharField(max_length = 65, verbose_name = 'Местоположение', default = 'Казахстан')

	img = models.ImageField(upload_to = 'static/img', blank = True)

	def __str__(self):
		return self.title