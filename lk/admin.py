from django.contrib import admin
from .models import Tarif, Module, Lesson

@admin.register(Tarif)
class TarifAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price']
    list_display_links = ['name']

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'tarif', 'open_date', 'close_date', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['tarif', 'open_date', 'close_date']
    list_display_links = ['name']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'module', 'video', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['module']
    search_fields = ['name', 'module__name']
    list_per_page = 20
    list_editable = ['video', 'module']
    list_display_links = ['name']
