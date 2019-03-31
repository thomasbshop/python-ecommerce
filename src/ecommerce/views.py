from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect


# relative import
from .forms import ContactForm, LoginForm, RegisterForm

# Create your views here. Views are created by functions or classes written in python

def home_page(request):
	# obj = Product.objects.get(id=1)
	

	context = {

		# "object": obj
		"content": "This is some content."
	
	}

	if request.user.is_authenticated():
		context["premium_content"] = "User is logged in."

	return render(request, "home_page.html", context)


def contact_page(request):
	# obj = Product.objects.get(id=1)
	
	contact_form = ContactForm(request.POST or None)

	context = {
		"title": "Contact",
		"content": "Welcome to the content page.",
		"form": contact_form,
		# "object": obj
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)

	# if request.method == "POST":
	# 	print(request.POST)
	# 	print(request.POST.get('firstName'))
	return render(request, "contact/view.html", context)


def about_page(request):
	# obj = Product.objects.get(id=1)
	

	context = {

		# "object": obj
	}
	return render(request, "home_page.html", context)