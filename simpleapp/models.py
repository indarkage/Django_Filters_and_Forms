from django.db import models
from django.core.validators import MinValueValidator
 
 
# Создаём модель товара 
class New(models.Model):
    author = models.CharField(
        max_length=200,
    )
    name = models.CharField(
        max_length=200,
        unique=True,
    )
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news', # все продукты в категории будут доступны через поле products
    )
 
    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self): # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}' 
 
 
#  создаём категорию, к которой будет привязываться товар
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # названия категорий тоже не должны повторяться
 
    def __str__(self):
        return f'{self.name.title()}'
