
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings
from django.urls import reverse


# class Buyer(AbstractUser):
#     middle_name = models.CharField(verbose_name="Отчество", max_length=50, blank=True, null=True)
#     # Пример внешнего ключа, если есть
#     # related_field = models.ForeignKey(OtherModel, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name} {self.middle_name or ""}'.strip()
#
#     class Meta:
#         verbose_name = "Покупатель"
#         verbose_name_plural = "Покупатели"



class MInstitutions(models.Model):
    name = models.CharField(verbose_name="Название", max_length=50)
    adress = models.CharField(verbose_name="Адресс", max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Учреждение"
        verbose_name_plural = "Учреждения"


class MService(models.Model):
    institutions = models.ForeignKey(MInstitutions, on_delete=models.CASCADE, verbose_name="Учреждение", blank=True,
                                     null=True)
    name = models.CharField(verbose_name="Название услуги", max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class MStaatus(models.Model):
    name = models.CharField(verbose_name="Статус", max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class MAppointments(models.Model):
    service = models.ForeignKey(MService, on_delete=models.CASCADE, verbose_name="Услуга", blank=True, null=True)
    organizations = models.ForeignKey(MInstitutions, on_delete=models.CASCADE, verbose_name="Учреждение", blank=True,
                                     null=True)
    date = models.DateField(verbose_name="Дата", blank=True, null=True, default=None)
    time = models.TimeField(verbose_name="Время", blank=True, null=True, default=None)
    status = models.ForeignKey(MStaatus, on_delete=models.CASCADE, verbose_name="Статус", blank=True,
                               null=True)

    def __str__(self):
        return f"{self.service}"

    class Meta:
        verbose_name = "Заявка пользователя"
        verbose_name_plural = "Заявки пользователей"


#
# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="User", on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     middle_name = models.CharField(max_length=100, blank=True)
#
#     def __str__(self):
#         return f"{self.first_name} {self.middle_name} {self.last_name}"


