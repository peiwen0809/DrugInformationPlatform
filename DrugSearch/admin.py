from django.contrib import admin
from DrugSearch.models import *


# Register your models here.
# 未使用
# 列出欄位
class ShowDrugCountry(admin.ModelAdmin):
    list_display = ('country_id', 'year', 'num')


class ShowDrugAge(admin.ModelAdmin):
    list_display = ('age_id', 'country_id', 'year', 'num')


class ShowDrugGender(admin.ModelAdmin):
    list_display = ('gender_id', 'country_id', 'year', 'num')


class ShowDrugType(admin.ModelAdmin):
    list_display = ('drug_id', 'country_id', 'year', 'num')


admin.site.register(DrugCountry, ShowDrugCountry)  # admin/admin123
admin.site.register(DrugAge, ShowDrugAge)
admin.site.register(DrugGender, ShowDrugGender)
admin.site.register(DrugType, ShowDrugType)