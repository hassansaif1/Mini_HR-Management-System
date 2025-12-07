from django.contrib import admin
from .models import LeaveRequest

# Register your models here.
@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ("start_date","end_date","reason","status", "created_at", "updated_at")
    list_filter = ("status", "created_at")
    search_fields = ("name", "email")
    ordering = ("-created_at",)