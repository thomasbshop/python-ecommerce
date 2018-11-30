from django import forms

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