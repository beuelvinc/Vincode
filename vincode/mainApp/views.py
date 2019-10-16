from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from  .models import Vincode,Image
from django import forms
# raise forms.ValidationError("The login details are incorrect")
# Create your views here.
class HomeView(TemplateView):
	template_name="home.html"
	def post(self,request,*args,**kwargs):
		vincode=self.request.POST.get("search-btn")
		
		data=Vincode.objects.filter(vincode_key=vincode).first()
		if data:
			vincode_id=data.vincode_key
			images=Image.objects.filter(vincode__vincode_key=vincode_id)
			return render(request, "home.html",{"data":data,"images":images})
		return render(request, "home.html")



		