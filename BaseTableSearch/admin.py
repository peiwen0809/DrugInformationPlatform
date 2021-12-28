from django.contrib import admin
from BaseTableSearch.models import *

# Register your models here.
class ShowAge(admin.ModelAdmin):
    list_display = ('age_id', 'age_range')

class ShowGender(admin.ModelAdmin):
    list_display = ('gender_id', 'gender')


admin.site.register(AgeTableSearch,ShowAge)
admin.site.register(GenderTableSearch,ShowGender)