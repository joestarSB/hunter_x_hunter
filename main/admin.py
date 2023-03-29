from django.contrib import admin

from .models import Gems, Category

class GemsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'balance']

admin.site.register(Gems, GemsAdmin)
admin.site.register(Category)