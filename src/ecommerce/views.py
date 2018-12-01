from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect


# relative import
from .forms import ContactForm, LoginForm, RegisterForm

# Create your views here. Views are created by functions or classes written in python

def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		"form": form
	}
	print("user logged in")
	print(request.user.is_authenticated())
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		
		user = authenticate(request, username=username, password=password)
		print(request.user.is_authenticated())
		if user is not None:
			print(request.user.is_authenticated())
			login(request, user)
			# Redirect to a success page.
			context["form"] = LoginForm()
			return redirect("/")
		else:
	    	# Return an 'invalid login' error message.
			print("error")

	return render(request, "auth/login.html", context)


User = get_user_model()
def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
		"form": form
	}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		new_user = User.objects.create_user(username, email, password)
		print(new_user)
		
	return render(request, "auth/register.html", context)


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