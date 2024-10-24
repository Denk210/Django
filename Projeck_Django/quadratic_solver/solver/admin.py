from django.contrib import admin

# Register your models here.

# myapp/admin.py
from django.contrib import admin
from .models import History

admin.site.register(History)