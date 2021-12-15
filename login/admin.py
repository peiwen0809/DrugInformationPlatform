from django.contrib import admin

# Register your models here.

from . import models


class ShowAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'password')


admin.site.register(models.Admin, ShowAdmin)
