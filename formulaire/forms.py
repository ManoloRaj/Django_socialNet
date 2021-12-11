from django.forms import ModelForm
from .models import user
from django import forms

#for inscription
class userForm(ModelForm):
    class Meta:
        model = user
        fields=['photo',  'first_name', 'family_name', 'user_name', 'password', 'date_of_birth', 'description']

        widgets = {
           
            'password': forms.PasswordInput(),
        }

class connexionForm(forms.Form):
    user_name = forms.CharField(max_length = 100)
    password = forms.CharField(max_length = 100)
    
    widgets = {
            
            'password': forms.PasswordInput(),
        }