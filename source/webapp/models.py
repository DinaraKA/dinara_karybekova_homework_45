from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class Task(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=20, verbose_name='Статус', default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)
    details = models.TextField(max_length=5000, null=False, blank=False, verbose_name='Детали')
    date = models.DateField(null=True, blank=True, default=None, verbose_name="Дата выполнения")


    def __str__(self):
        return "{}. {}".format(self.pk, self.description)

