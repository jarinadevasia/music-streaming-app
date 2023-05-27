from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Song)
admin.site.register(Registration)
admin.site.register(Artist)
admin.site.register(Category)
admin.site.register(Favorite)