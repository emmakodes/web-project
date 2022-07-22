from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm


# Create your views here.
def index(request):
    return render(request, "firstapp/index.html")

@login_required
def contact(request):
    if request.method == "POST":
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contactform.save()
            messages.success(request, 'Message saved successfully, thank you')
            return redirect("firstapp:index")
    else:
        contactform = ContactForm()

        # name = request.POST.get("name")
        # phone = request.POST.get("phone")
        # message = request.POST.get("message")
        # contacts = Contact(name=name, phone=phone, message=message)
        # contacts.save()
        # messages.success(request, 'Message saved successfully, thank you')
        # return redirect("firstapp:index")

    context = {
        "contactform" : contactform,
    }

    return render(request, "firstapp/contactus.html", context)