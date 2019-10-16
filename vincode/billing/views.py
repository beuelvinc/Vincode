from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.mail import send_mail
from contactApp.tasks import send_feedback_email_task

stripe_mail='Balansınızdan 2 dollar çıxıldı,xidmətdən istifadə etdiyiniz üçün təşəkkürlər'

import stripe
STRIPE_PUBLISHABLE_KEY='pk_test_9ilTMuHdNQ46Ingn8mXxMe9x00HzIAPpaT'
def billing(request):
	if request.method=="POST":
		try:
			stripe.api_key = 'sk_test_X7fFSirQyCXoPGMijYkS9AFL00Dg3u7pIP'
			token = request.POST['stripeToken'] # Using Flask
			email = request.POST['email'] # Using Flask
			print(email)
			send_mail(
				'Vincode',
				stripe_mail,
				'elvinc402@gmail.com',
				[email],
				fail_silently=False,
			)
			# send_feedback_email_task.delay(
			# 	"Vincode",email,stripe_mail
			# )
			charge = stripe.Charge.create(
				amount=200,
				currency='usd',
				description='Example charge',
				source=token,
			)
		except :
			print("sadsa")
	return render(request,"billing.html",{"publish_key":STRIPE_PUBLISHABLE_KEY})


