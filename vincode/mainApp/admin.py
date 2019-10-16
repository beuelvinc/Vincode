from django.contrib import admin

# Register your models here.
from  .models import Vincode,Image

admin.site.register(Vincode)
admin.site.register(Image)
