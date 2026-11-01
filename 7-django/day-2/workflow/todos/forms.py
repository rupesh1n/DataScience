from django import forms
from .models import ToDo

class UserForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='User Name:')
    email = forms.CharField(max_length=100, required=True, label='Email:')
    age = forms.IntegerField(label = 'Age:')
    
class TodoForm(forms.ModelForm):
    class Meta:
        model=ToDo
        fields=['title', 'description', 'done', 'deadline', 'priority']

        wedgets= {
            'dedline': forms.DateInput(attrs={'type':'date'})
        }