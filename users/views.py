from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import  render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("firstapp:contact")
		#messages.error(request, "Unsuccessful registration. Invalid information.")
		#print(form.errors)
		# print(form.errors)
	else:
		form = RegisterForm()

	context = {
		"form": form,
	}
	return render(request, "users/register.html", context)

def loginusers(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("firstapp:contact")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	else:
		form = AuthenticationForm()
	print(form)
	context = {
		"loginform" : form,
	}
	return render(request, "users/login.html", context)

def logoutusers(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("firstapp:index")