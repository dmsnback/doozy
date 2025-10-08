from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


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
        blank=True,
        null=True,
        help_text='Укажите срок выполнения задачи'
    )
    priority = models.ForeignKey(
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
        null=True,
        related_name='author',
        verbose_name='Пользователь'
    )


    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
    
    def time_left(self):
        now = timezone.now()
        if self.finish_at:
            deadline = self.finish_at - now
            day = deadline.days
            hour = deadline.seconds // 3600
            minute = (deadline.seconds % 3600) // 60
            if deadline.total_seconds() < 0:
                return 'Просрочено'
            elif day > 0:
                return f'Осталось: {day} дн. {hour}ч.'
            elif hour > 0:
                return f'Осталось: {hour}ч. {minute} мин.'
            elif minute > 0:
                return f'Осталось: {minute}мин.'
            return 'Осталось: менее часа...'
