from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields =('name','details')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control',  'rows': 4}),
        }
        labels = {
            'name': 'Task Name',
            'details': 'Task Description',
        }
        help_texts = {
            'name': 'Enter a descriptive task name.',
            'details': 'Provide details or notes about the task.',
        }