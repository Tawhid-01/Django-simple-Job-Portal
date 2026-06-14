from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username','display_name', 'email','user_type', 'password1', 'password2']
        
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for i_name, i in self.fields.items():
         i.widget.attrs['class'] = 'form-control'
    
        
     


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password1']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for i_name, i in self.fields.items():
         i.widget.attrs['class'] = 'form-control'
        


class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = JobSeekerModel
        fields = "__all__"
        exclude = ['user']
        widgets = {
            'skills': forms.CheckboxSelectMultiple(),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for i_name, i in self.fields.items():
         i.widget.attrs['class'] = 'form-control'

class RecruiterForm(forms.ModelForm):
    class Meta:
        model = RecruiterModel
        fields = "__all__"
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for i_name, i in self.fields.items():
         i.widget.attrs['class'] = 'form-control'

class JobForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = "__all__"
        exclude = ['user']
        widgets = {
            'skills': forms.CheckboxSelectMultiple(),
        }
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for i_name, i in self.fields.items():
         i.widget.attrs['class'] = 'form-control'
         

class SkillForm(forms.ModelForm):
    class Meta:
        model = SkillModel
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for i_name, i in self.fields.items():
         i.widget.attrs['class'] = 'form-control'