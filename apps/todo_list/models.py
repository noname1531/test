from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True) 
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    completed = models.BooleanField(
        default=False,
        verbose_name='Завершено'
    )
    created = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата создания'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'