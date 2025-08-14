from django import forms

from tasks.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        exclude = ('created_at', 'completed', 'author')
        widgets = {
            'comment': forms.Textarea(
                {'cols': '22', 'rows': '5'},
            ),
            'finish_at': forms.DateTimeInput(
                attrs={'type': 'date'}
            )
        }
