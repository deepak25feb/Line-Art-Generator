from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255,primary_key=True)
    password = models.CharField(max_length=255)
    emailid = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)

#One to Many Relationship 
class Photos(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True,upload_to='usersphotos/')
    #timestampcreated = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return str(self.username)


class ConvertedPhotos(models.Model):
    photooriginal = models.OneToOneField(Photos,on_delete=models.CASCADE,primary_key=True)
    imageconverted = models.ImageField(null=True,blank=True,upload_to='converted/')
    timestampcreated = models.DateTimeField(auto_now_add=True,null=True)
