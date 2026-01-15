from django.contrib import admin
from .models import Procedure

@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ("title", "updated_at", "is_published")
    list_filter = ("is_published",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}