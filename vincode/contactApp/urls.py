from django.urls import path,include
from .views import ContactView

app_name="contactApp"
urlpatterns = [
    path("",ContactView,name="contact")
]
