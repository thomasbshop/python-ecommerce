from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
	"""docstring for ContactForm
		Form is a built-in django class for form."""
	firstName  = forms.CharField(
		widget=forms.TextInput(
			attrs={
			"class": "form-control",
			"placeholder": "your first name..."
			}
		  )
		)
	email      = forms.EmailField(
		widget=forms.EmailInput(
			attrs={
			"class": "form-control",
			"placeholder": "your email..."
			}
		  )
		)
	content = forms.CharField(
		widget=forms.Textarea(
			attrs={
			"class": "form-control",
			"placeholder": "your message..."
			}
		  )
		)

	def clean_email(self):  # to add custom validation.
		email = self.cleaned_data.get("email")
		if not "gmail.com" in email:
			raise forms.ValidationError("Email has to be gmail.com")
		return email


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