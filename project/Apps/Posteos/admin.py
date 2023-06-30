from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Posteos)
class PosteosAdmin(admin.ModelAdmin):
    list_display = ("titulo",)
    search_fields = ("titulo",)
    list_filter = ("titulo",)
    ordering = ("titulo",)