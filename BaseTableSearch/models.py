from django.db import models

# Create your models here.
#資料表裡有的欄位
class AgeTableSearch(models.Model):
    age_id = models.IntegerField(primary_key=True)
    age_range = models.TextField()

    class Meta:
        db_table = "age"

    # 取得年齡層欄位
    def getTable(**kwargs):
        table = kwargs.get('table')
        result = AgeTableSearch.objects.raw('SELECT * FROM age WHERE age_id IN (6,8,9,10,11,13,14)')
        return result


class GenderTableSearch(models.Model):
    gender_id = models.IntegerField(primary_key=True)
    gender = models.TextField()

    class Meta:
        db_table = "gender"

    # 取得性別欄位
    def getTable(**kwargs):
        table = kwargs.get('table')
        result = GenderTableSearch.objects.raw('SELECT * FROM gender')
        return result