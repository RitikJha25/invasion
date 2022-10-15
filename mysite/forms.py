from django import forms
from .models import MakeBlogs, Comments
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]

class createBlogs(forms.ModelForm):
	title = forms.CharField(max_length = 10000)
	description = forms.CharField(max_length = 100000000, widget = forms.Textarea({"rows" :30, "cols":100}))
	reference = forms.CharField(max_length = 10000)
	class Meta:
		model = MakeBlogs
		fields = ["title","description", "reference"]



class EditProfileForm(UserChangeForm):


	class Meta:
		model = User
		fields = ["first_name", "last_name"]

class commentForm(forms.ModelForm):
	comment= forms.CharField(max_length = 100000000)
	class Meta:
		model = Comments
		fields = ['comment']

