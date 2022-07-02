from django import forms
from .models import *
  
class MentorForm(forms.ModelForm):
  
    class Meta:
        model = mentor
        fields = ['sid', 'sname', 'batch', 'placed', 'about', 'img']
        