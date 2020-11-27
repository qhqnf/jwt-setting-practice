from django.contrib import admin
from .models import StopWord

@admin.register(StopWord)
class StopWordAdmin(admin.ModelAdmin):
    pass