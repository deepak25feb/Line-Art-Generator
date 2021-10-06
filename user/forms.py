from django.db.models import fields
from django.forms import ModelForm
from .models import *

class PhotosForm(ModelForm):
    class Meta:
        model = Photos
        fields = ['image']
        #fields = '__all__'

class ProfilePhotosForm(ModelForm):
    class Meta:
        model = ProfilePhotos
        fields = ['profilephoto']
        #fields = '__all__'