from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Platform)
admin.site.register(Edition)
admin.site.register(Game)
admin.site.register(Comment)