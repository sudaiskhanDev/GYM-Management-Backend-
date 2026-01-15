from django.contrib import admin
from .models import MemberModel
# Register your models here.
@admin.register(    MemberModel)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'join_date', 'is_active')