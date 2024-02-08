from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("content", "datetime", "deadline", "tags")
        widgets = {"deadline": forms.DateInput()}

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields["deadline"].required = False
