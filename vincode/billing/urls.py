from django.urls import path,include
from .views import billing
app_name='billing'
urlpatterns = [
path("",billing,name='billing')
] 
