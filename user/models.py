from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    emailid = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)

#One to Many Relationship 
class Photos(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True,upload_to='usersphotos/')
    imageconverted = models.ImageField(null=True,blank=True,upload_to='converted/')
    def __str__(self):
        return str(self.username)


class ProfilePhotos(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    profilephoto = models.ImageField(null=True,blank=True,upload_to='usersphotos/',default="default.png")
    def __str__(self):
        return str(self.username)



