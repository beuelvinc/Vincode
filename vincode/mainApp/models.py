from django.db import models

# Create your models here.
class Vincode(models.Model):
    vincode_key=models.CharField(max_length=20,default='')
    Make=models.CharField(max_length=150)
    Model=models.CharField(max_length=150)
    Color=models.CharField(max_length=150)
    Engine=models.CharField(max_length=150)
    Condition=models.CharField(max_length=150)
    Primary_damage=models.CharField(max_length=150)
    Secondary_damage=models.CharField(max_length=150)
    def __str__(self):
        return self.Make+" "+self.Model
def get_image_filename(instance, filename):
    id = instance.vincode.id
    return "post_images/image-%s" % (id)  


class Image(models.Model):
    vincode = models.ForeignKey(Vincode, on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')
    def __str__(self):
        return self.vincode.Make+" "+self.vincode.Model 