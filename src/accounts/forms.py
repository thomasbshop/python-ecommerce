from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
	"""docstring for LoginForm"""
	username = forms.CharField()
	password = forms.CharField(
		widget=forms.PasswordInput
		)

class RegisterForm(forms.Form):
	"""docstring for LoginForm"""
	email  = forms.EmailField(
		widget=forms.EmailInput(
			attrs={
			"class": "form-control",
			"placeholder": "your email..."
			}
		  )
		)
	username = forms.CharField()
	password = forms.CharField(
		widget=forms.PasswordInput
		)
	password2 = forms.CharField(
		label='confirm password',
		widget=forms.PasswordInput
		)

	
	def clean_username(self):  # to add custom validation.
		username = self.cleaned_data.get("username")
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("Username is taken.")
		return username


	def clean_email(self):  # to add custom validation.
		email = self.cleaned_data.get("email")
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("Email is taken.")
		return email

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password2 != password:
			raise forms.ValidationError("Passwords must match.")
		return data
