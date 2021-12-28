from django.contrib import admin
from DrugNews import models
# Register your models.
class ShowNews(admin.ModelAdmin):
    list_display = ('id', 'title', 'link')
admin.site.register(models.NewsList, ShowNews)
# admin.site.register(models.NewsList)
