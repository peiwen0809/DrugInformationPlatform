# Register your models here.
from django.contrib import admin
from DrugIntro.models import DrugIntro

# admin.site.register(DrugIntro)

#列出欄位
class ShowDrugInfo(admin.ModelAdmin):
    list_display = ('drug_id', 'ch_name', 'en_name', 'drug_intro', 'img1', 'img2', 'img3')

admin.site.register(DrugIntro, ShowDrugInfo)  #admin/admin123
