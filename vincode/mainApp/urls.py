from django.urls import path,include
from .views import HomeView
app_name="mainApp"
urlpatterns = [
    path("",HomeView.as_view(),name="home"),
]
