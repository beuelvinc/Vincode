from django.urls import path,include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('vincode', views.VincodeViewSet)
router.register('vincode-images', views.ImageViewSet)
app_name='rest_api'
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]