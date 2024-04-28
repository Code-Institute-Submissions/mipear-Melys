from django import forms
from .models import WorkshopApply

class ApplyForm(forms.ModelForm):
    class Meta:
        model = WorkshopApply
        fields = ('name', 'user', 'age', 'reason', 'email',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Which workshop are you interested in?',
            'user': 'Full Name',
            'age': 'Age',
            'reason': 'Why are you interested in this workshop?',
            'email': 'Email',
        }