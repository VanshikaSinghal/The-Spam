from django.contrib import admin

from .models import Ham, Spam

# Register your models here.
admin.site.register([Ham, Spam])