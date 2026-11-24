from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ("ticket_id", "category", "area", "status", "created_at")
    list_filter = ("status", "category", "created_at")
    search_fields = ("ticket_id", "name", "email", "address", "area")
    readonly_fields = ("ticket_id", "created_at", "updated_at")
    list_editable = ("status",)
