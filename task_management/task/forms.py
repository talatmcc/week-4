from django import forms
from .models import Task
from category.models import TaskCategory

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['taskTitle', 'taskDescription', 'is_completed', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
        }

    categories = forms.ModelMultipleChoiceField(
        queryset=TaskCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
