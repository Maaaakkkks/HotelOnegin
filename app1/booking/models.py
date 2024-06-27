from django.db import models
from users.models import Users
# Create your models here.


# Прмиер
# class Categories(models.Model):
#     name = models.CharField(max_length=150, unique=True, verbose_name = 'Название')
#     slug = models.SlugField(max_length=200, unique=True, blank=True, null= True, verbose_name = 'URL')

#     class Meta:
#         db_table = 'category'
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'


class Rooms(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name = 'Название')
    person_max = models.IntegerField( verbose_name = 'Макс количество взрослых', default=0)
    child_max = models.IntegerField( verbose_name = 'Макс количество детей', default=0)
    room_class = models.IntegerField(verbose_name = 'Тип номера', default=0)
    room_number = models.IntegerField(verbose_name = 'Номер комнаты', default=0)
    class Meta:
        db_table = 'Rooms'
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'

        def __str__(self) -> str:
            return f'{self.name} Количество - {self.quantity}'
        

# class Rooms_descript(models.Model):
#     name = models.CharField(max_length=150, unique=True, verbose_name = 'Название')
#     room_class = models.IntegerField(verbose_name = 'Тип номера', default=0)
#     desc1 = models.CharField(max_length=300, unique=False, null=True)
#     desc2 = models.CharField(max_length=300, unique=False, null=True)
#     desc3 = models.CharField(max_length=300, unique=False, null=True)
#     desc4 = models.CharField(max_length=300, unique=False, null=True)
#     desc5 = models.CharField(max_length=300, unique=False, null=True)
#     desc6 = models.CharField(max_length=300, unique=False, null=True)
#     desc7 = models.CharField(max_length=300, unique=False, null=True)
#     desc8 = models.CharField(max_length=300, unique=False, null=True)
#     desc9 = models.CharField(max_length=300, unique=False, null=True)
#     desc10 = models.CharField(max_length=300, unique=False, null=True)
    
    
#     class Meta:
#         db_table = 'Rooms_descript'
#         verbose_name = 'Описание номеров'
#         verbose_name_plural = 'Описания номеров'

#         def __str__(self) -> str:
#             return f'{self.name} Количество - {self.quantity}'


# Надо сделать миграции
class Booking(models.Model):
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    room = models.ForeignKey(to=Rooms, on_delete=models.CASCADE)
    date_in = models.DateField
    date_out = models.DateField
    person = models.IntegerField(max_length=10, verbose_name = 'Название')
    child = models.IntegerField(max_length=10, verbose_name = 'Название')