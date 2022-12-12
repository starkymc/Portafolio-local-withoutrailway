from django.contrib import admin
from .models import Portafolio

# Register your models here.
class PortafolioAdmin(admin.ModelAdmin):
    admin.site.register(Portafolio)