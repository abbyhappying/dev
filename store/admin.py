from django.contrib import admin

# Register your models here.

from .models import Category,Products

# admin.site.register(Category)
# admin.site.register(Products)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
