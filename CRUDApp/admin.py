from django.contrib import admin
from .models import Member
# Register your models here.

class modelAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","country")

admin.site.register(Member, modelAdmin)