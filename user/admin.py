from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Photos) # Store All User Uploaded Normal Images 
admin.site.register(ConvertedPhotos) # Store All User Converted Art Line Images 
