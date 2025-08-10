from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class PriorityTask(models.Model):
    """Модель приоритета задачи"""

    title = models.CharField(
        'Приолритет задачи',
        max_length=56,
        default='Низкий'
    )

    class Meta:
        verbose_name = 'Приоритет задачи'
        verbose_name_plural = 'Приоритеты задачи'

    def __str__(self):
        return self.title


class Task(models.Model):
    """Модель задачи"""

    title = models.CharField(
        'Название задачи',
        max_length=256,
        help_text='Введите название задачи'
    )
    comment = models.TextField(
        'Комментарий к задаче',
        blank=True,
        help_text='Напиште комментарий к задаче, если это нужно.'
    )
    completed = models.BooleanField(
        'Выполнено',
        default=False,
        help_text='Статус выполнения задачи'
    )
    created_at = models.DateTimeField(
        'Дата создания задачи',
        auto_now_add=True
    )
    finish_at = models.DateTimeField(
        'Срок выполнения задачи',
        help_text='Укажите срок выполнения задачи'
    )
    prioroty = models.ForeignKey(
        PriorityTask,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='priorities',
        verbose_name='Приоритет задачи',
        help_text='Выберите приоритет задачи'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='Пользователь'
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ('created_at', '-completed',)

    def __str__(self):
        return self.title
