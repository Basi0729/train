
from django import forms
from django.forms import ModelForm
from articles.models import Profile
from django.contrib.auth.forms import  *
from django.contrib.auth.models import User

class NewProfile(ModelForm):
    class Meta:
        model=Profile
        fields=('name',"age","occupation",'place',
        'joining_date','email_id','profile_Main_Img')

class NewUserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ("username",  "password1", "password2")