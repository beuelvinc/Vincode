from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from vincode import settings
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("mainApp.urls",namespace="mainApp")),
    path("contact/",include("contactApp.urls",namespace="contactApp")),
    path("billing/",include("billing.urls",namespace="billing")),
    path("rest/",include("rest_api.urls",namespace="rest_api")),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


