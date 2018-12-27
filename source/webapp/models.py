from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=True,related_name='employee', verbose_name="Сотрудник")
    phone = models.CharField(max_length=50, verbose_name="Телефон")

    def __str__(self):
        return self.user.get_full_name()



class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название блюда")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    photo = models.ImageField(verbose_name='Фотография')

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in progress'
    STATUS_IN_DELIVERY = 'beeing delivered'
    STATUS_DONE = 'done'
    STATUS_CANCELLED = 'cancelled'


    STATUS_CHOICES = (
        (STATUS_NEW, 'новый'),
        (STATUS_IN_PROGRESS, 'в процессе'),
        (STATUS_IN_DELIVERY, 'доставляется'),
        (STATUS_DONE, 'выполненный'),
        (STATUS_CANCELLED, 'отменен')
    )

    client_name = models.CharField(max_length=50, verbose_name="Имя клиента")
    client_phone = models.CharField(max_length=50, verbose_name="Телефон")
    client_address = models.CharField(max_length=50, verbose_name="Адрес")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name="Статус", default=STATUS_NEW)
    operator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='operator_orders', verbose_name='Оператор')
    courier = models.ForeignKey(User, on_delete=models.PROTECT, related_name='courier_orders', verbose_name='Курьер')

    def __str__(self):
        return self.client_phone



class CourseOrder(models.Model):
    order = models.ForeignKey(Order, related_name='courses', verbose_name='Заказ', on_delete=models.PROTECT)
    course = models.ForeignKey(Course, related_name='ordered', verbose_name='Блюдо', on_delete=models.PROTECT)
    quantity = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return str(self.course)
