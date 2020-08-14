from django.db import models

# Create your models here.


class User(models.Model):
    mid = models.CharField('mid', max_length=100)
    name = models.CharField('name', max_length=800)
    sign = models.CharField('sign', max_length=800, blank=True, null=True)
    level = models.CharField('level' , max_length=10)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = 'User'

    def __str__(self):
        return self.name
