from distutils.command.upload import upload
from django.db import models

# Create your models here.
class mentor(models.Model):
    sid = models.IntegerField(primary_key=True)
    sname= models.CharField(max_length=70)
    batch = models.IntegerField()
    placed = models.CharField(max_length=70) 
    about = models.TextField() 
    img = models.ImageField(upload_to='images/')    

    def __str__(self):
        return self.title    

