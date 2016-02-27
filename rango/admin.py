from django.contrib import admin
from rango.models import UserProfile,Message


# Add in this class to customized the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


# Update the registeration to include this customised interface

admin.site.register(Message)
admin.site.register(UserProfile)
