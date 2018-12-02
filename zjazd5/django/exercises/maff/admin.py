from django.contrib import admin
from maff.models import maff

# Register your models here.

class Maffadmin(admin.ModelAdmin):
    listdisplay=["funk","int1","int2"]
    search_fields=["funk"]

admin.site.register(maff,Maffadmin)

