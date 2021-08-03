from django.contrib import admin
from .models import Team

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    display_list=['first_name','job','created_date'],
admin.site.register(Team,TeamAdmin)
