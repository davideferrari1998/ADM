from django.http import HttpRequest, HttpResponse
from django.shortcuts import  render, redirect
from carrello.models import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return HttpResponse("Registrazione effettuata con successo")
		return HttpResponse("Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="ecommerce/register.html", context={"register_form":form})