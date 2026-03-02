from django.contrib import admin
from .models import Watch


@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at', 'price']
    ordering = ['-created_at']
