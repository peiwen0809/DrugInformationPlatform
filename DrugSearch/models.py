from django.db import models

# Create your models here.
#資料表裡有的欄位
class DrugCountry(models.Model):
    # PK應該為country_id, year，但Django windows不支持多列主鍵，因此先將country_id設定為主鍵，再設定country_id+year為unique
    country_id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    num = models.IntegerField()

    class Meta:
        unique_together = (('country_id', 'year'),)
        db_table = "country_year_num"

    # 從表中查詢一個國家每年的吸毒人數
    def countryYearNum(**kwargs):
        country_id = kwargs.get('country_id')
        result = DrugCountry.objects.raw('SELECT * FROM country_year_num WHERE country_id = %s ORDER BY year', [country_id])
        return result


class DrugAge(models.Model):
    # PK應該為country_id, year，但Django windows不支持多列主鍵，因此先將country_id設定為主鍵，再設定country_id+year為unique
    country_id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    # age = models.ForeignKey(Age,on_delete=models.CASCADE)
    age_id = models.IntegerField()
    num = models.IntegerField()

    class Meta:
        unique_together = (('country_id', 'year','age_id'),)
        db_table = "age_num"

    # 從表中查詢一個國家每年的吸毒人數，依性別區分
    def ageNum(**kwargs):
        country_id = kwargs.get('country_id')
        # 211207-001 修改age table的欄位名稱
        result = DrugAge.objects.raw('SELECT age_num.country_id,age_num.year,age.age_range,age_num.num,age.age_id FROM age_num,age WHERE age_num.age_id=age.age_id AND age_num.country_id = %s ORDER BY year',
                                         [country_id])
        return result

class DrugGender(models.Model):
    # PK應該為country_id, year，但Django windows不支持多列主鍵，因此先將country_id設定為主鍵，再設定country_id+year為unique
    country_id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    gender_id = models.IntegerField()
    num = models.IntegerField()

    class Meta:
        unique_together = (('country_id', 'year','gender_id'),)
        db_table = "gender_num"

    # 從表中查詢一個國家每年的吸毒人數，依性別區分
    def genderNum(**kwargs):
        country_id = kwargs.get('country_id')
        # 211207-001 gender table的欄位名稱
        result = DrugGender.objects.raw('SELECT gender_num.country_id, gender_num.num, gender_num.year, gender.gender, gender_num.gender_id FROM gender_num,gender WHERE gender_num.gender_id = gender.gender_id AND country_id = %s ORDER BY year',
                                         [country_id])
        return result


class DrugType(models.Model):
    # PK應該為country_id, year，但Django windows不支持多列主鍵，因此先將country_id設定為主鍵，再設定country_id+year為unique
    country_id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    drug_id = models.IntegerField()
    num = models.IntegerField()

    class Meta:
        unique_together = (('country_id', 'year','drug_id'),)
        db_table = "drug_num"

    # 從表中查詢一個國家每年的吸毒人數，依毒品種類區分
    def drugTypeNum(**kwargs):
        country_id = kwargs.get('country_id')
        # 211207-001 drug type table的欄位名稱
        result = DrugAge.objects.raw('SELECT drug_num.country_id,drug_num.year,drug_type.ch_name,drug_num.num, drug_num.drug_id FROM drug_num,drug_type WHERE drug_num.drug_id=drug_type.drug_id AND drug_num.country_id = %s ORDER BY year',
                                         [country_id])
        return result