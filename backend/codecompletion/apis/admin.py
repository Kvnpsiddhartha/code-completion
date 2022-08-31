from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone','photo']
    search_fields=['username']
    # list_filter = ['designation']
    ordering = ['username']

@admin.register(Folder)
class FoldersAdmin(admin.ModelAdmin):
    list_display = ['get_user_name','get_parent_folder','name', 'modified_time']
    search_fields=['name']
    list_filter = ['parent_folder__name','user__username']
    ordering = ['name']
    @admin.display(ordering='parent_folder__name', description='Parent Folder')
    def get_parent_folder(self, obj):
            return obj.parent_folder.name
    @admin.display(ordering='user__username', description='User')
    def get_user_name(self, obj):
            return obj.user.username
@admin.register(Program)
class ProgramsAdmin(admin.ModelAdmin):
    list_display = ['name', 'modified_time']
    search_fields=['name']
    # list_filter = ['designation']
    ordering = ['name']
    @admin.display(ordering='parent_folder__name', description='Parent Folder')
    def get_parent_folder(self, obj):
            return obj.parent_folder.name
    @admin.display(ordering='user__username', description='User')
    def get_user_name(self, obj):
            return obj.user.username