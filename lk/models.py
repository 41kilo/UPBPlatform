from django.db import models

# Create your models here.
class Tarif(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'
    
    def __str__(self):
        return self.name

class Module(models.Model):
    tarif = models.ForeignKey(Tarif, related_name='modules', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    open_date = models.DateField()
    close_date = models.DateField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'

    def __str__(self):
        return self.name
    
class Lesson(models.Model):
    module = models.ForeignKey(Module, related_name='lessons', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    video = models.FileField(upload_to='lessons/')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
    
    def __str__(self):
        return self.name
    
    

модуль
название

урок
название
модуль

тариф
название
модуль 
