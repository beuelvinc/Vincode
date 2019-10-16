from django.shortcuts import render,redirect
from .forms import ContactForm
from django.core.mail import send_mail
from .tasks import send_feedback_email_task
from django.contrib import messages

def ContactView(request):
	form=ContactForm()
	if request.method=="POST":
		form=ContactForm(request.POST or None)
		if form.is_valid():
			name=form.cleaned_data.get("name")
			email=form.cleaned_data.get("email")
			message=form.cleaned_data.get("message")
			send_feedback_email_task.delay(
				name,email,message
			)
			messages.success(request, 'Mesajınız uğurla göndərildi.')
			form=ContactForm()
			return redirect("mainApp:home")
	return render(request,"contact.html",{"form":form})