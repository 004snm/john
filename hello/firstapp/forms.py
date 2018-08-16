from django import forms
from firstapp.models import*
class LoginForm(forms.ModelForm):

	class Meta:
		model=Login
		fields='__all__'
class RegisterForm(forms.ModelForm):

	class Meta:
		model=Register
		fields='__all__'