from django.db import models
import uuid


class Poll(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=True, help_text='Уникальный ID пользователя')
    poll = models.CharField(max_length=200, help_text='Название опроса')
    description = models.CharField(max_length=200, help_text='Описание опроса')
    start_date = models.DateField('Дата начала опроса')
    finish_date = models.DateField('Дата окончания опроса', blank=True)

    def __str__(self):
        return self.poll


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.SET_NULL, null=True)
    question = models.CharField(max_length=200, help_text='Вопрос')
    choice = models.CharField(max_length=200, help_text='Варианты ответа')
    votes = models.CharField(max_length=20, blank=True, help_text='Введите ответ')
    CHOICE_TYPE = (
        ('1', 'Ответ текстом'),
        ('2', 'ответ с выбором одного варианта'),
        ('3', 'ответ с выбором нескольких вариантов'),
    )
    TypeOfChoice = models.CharField(max_length=1, choices=CHOICE_TYPE, default='1', help_text='Выбор типа ответа',)

    def __str__(self):
        """String for representing the Model object."""
        return self.question
