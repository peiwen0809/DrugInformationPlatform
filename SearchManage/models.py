from django.db import models
from DrugSearch import models as m


# Create your models here.
# 資料表裡有的欄位
class DrugCountry(models.Model):
    # # PK應該為country_id, year，但Django windows不支持多列主鍵，因此先將country_id設定為主鍵，再設定country_id+year為unique
    # country_id = models.IntegerField(primary_key=True)
    # year = models.IntegerField()
    # num = models.IntegerField()
    #
    # class Meta:
    #     unique_together = (('country_id', 'year'),)
    #     db_table = "country_year_num"

    # 從表中修改一個國家每年的吸毒人數
    # {"country_id":1,"year":"2020","num":20000}
    def countryYearNum(**kwargs):
        country_id = kwargs.get('country_id')
        year = kwargs.get('year')
        num = kwargs.get('num')
        try:
            # a = m.DrugCountry.objects.get(country_id=country_id, year=year)
            # a.num = num
            # a.save()
            post = m.DrugCountry.objects.filter(country_id=country_id, year=year)
            if not post:
                return "資料不存在，請重新輸入"
            else:
                post.update(num=num)
        except m.DrugCountry.DoesNotExist:
            return False
        else:
            return True

    def createCountryYearNum(**kwargs):
        country_id = kwargs.get('country_id')
        year = kwargs.get('year')
        num = kwargs.get('num')
        try:
            ins = m.DrugCountry.objects.filter(country_id=country_id, year=year)
            if ins:
                return "資料已經存在，請重新輸入"
            m.DrugCountry.objects.create(country_id=country_id, year=year, num=num)
            # ins.save()
        except Exception as e:
            print(e)
            return False
        return True


class DrugAge(models.Model):
    # PK應該為country_id, year，但Django windows不支持多列主鍵，因此先將country_id設定為主鍵，再設定country_id+year為unique
    # country_id = models.IntegerField(primary_key=True)
    # year = models.IntegerField()
    # # age = models.ForeignKey(Age,on_delete=models.CASCADE)
    # age_id = models.IntegerField()
    # num = models.IntegerField()
    #
    # class Meta:
    #     unique_together = (('country_id', 'year', 'age_id'),)
    #     db_table = "age_num"

    # 從表中修改一個國家每年的吸毒人數，依年齡區分
    # {"country_id":1,"year":"2020","data":[{"age_id":1,"num":20000},{"age_id":2,"num":20000},{...}]}
    def ageNum(**kwargs):
        age_id = kwargs.get('age_id')
        country_id = kwargs.get('country_id')
        year = kwargs.get('year')
        num = kwargs.get('num')
        try:
            # a = m.DrugAge.objects.get(age_id=age_id, country_id=country_id, year=year)
            # a.num = num
            # a.save()
            post = m.DrugAge.objects.filter(country_id=country_id, year=year, age_id=age_id)
            print(post)
            if not post:
                return "資料不存在，請重新輸入"
            post.update(num=num)
        except m.DrugAge.DoesNotExist:
            return False
        return True

    def createAgeNum(**kwargs):
        age_id = kwargs.get('age_id')
        country_id = kwargs.get('country_id')
        year = kwargs.get('year')
        num = kwargs.get('num')
        try:
            ins = m.DrugAge.objects.filter(country_id=country_id, year=year, age_id=age_id)
            if ins:
                return "資料已經存在，請重新輸入!"
            m.DrugAge.objects.create(age_id=age_id, country_id=country_id, year=year, num=num)
            # ins.save()
        except Exception:
            return False
        return True


class DrugGender(models.Model):
    # # PK應該為country_id, year，但Django windows不支持多列主鍵，因此先將country_id設定為主鍵，再設定country_id+year為unique
    # country_id = models.IntegerField(primary_key=True)
    # year = models.IntegerField()
    # gender_id = models.IntegerField()
    # num = models.IntegerField()
    #
    # class Meta:
    #     unique_together = (('country_id', 'year', 'gender_id'),)
    #     db_table = "gender_num"

    # 從表中修改一個國家每年的吸毒人數，依性別區分
    # {"country_id":1,"year":"2020","data":[{"gender":"male","num":20000},{"gender":"female","num":20000}]}
    def genderNum(**kwargs):
        gender_id = kwargs.get('gender_id')
        country_id = kwargs.get('country_id')
        year = kwargs.get('year')
        num = kwargs.get('num')
        try:
            # a = m.DrugGender.objects.get(country_id=country_id, year=year, gender_id=gender_id)
            # a.num = num
            # a.save()
            post = m.DrugGender.objects.filter(country_id=country_id, year=year, gender_id=gender_id)
            if not post:
                return "資料不存在，請重新輸入!"
            post.update(num=num)
        except m.DrugGender.DoesNotExist:
            return False
        return True

    def createGenderNum(**kwargs):
        gender_id = kwargs.get('gender_id')
        country_id = kwargs.get('country_id')
        year = kwargs.get('year')
        num = kwargs.get('num')
        try:
            ins = m.DrugGender.objects.filter(country_id=country_id, year=year, gender_id=gender_id)
            if ins:
                return "資料已經存在，請重新輸入!"
            m.DrugGender.objects.create(country_id=country_id, year=year, gender_id=gender_id, num=num)
            # ins.save()
        except Exception:
            return False
        return True


class DrugType(models.Model):
    # PK應該為country_id, year，但Django windows不支持多列主鍵，因此先將country_id設定為主鍵，再設定country_id+year為unique
    # country_id = models.IntegerField(primary_key=True)
    # year = models.IntegerField()
    # drug_id = models.IntegerField()
    # num = models.IntegerField()
    #
    # class Meta:
    #     unique_together = (('country_id', 'year', 'drug_id'),)
    #     db_table = "drug_num"

    # 從表中修改一個國家每年的吸毒人數，依毒品種類區分
    # {"country_id":1,"year":"2020","data":[{"drug_id":1,"num":20000},{"drug_id":2,"num":20000},{...}]}
    def drugTypeNum(**kwargs):
        drug_id = kwargs.get('drug_id')
        country_id = kwargs.get('country_id')
        year = kwargs.get('year')
        num = kwargs.get('num')
        try:
            # a = m.DrugType.objects.get(country_id=country_id, year=year, drug_id=drug_id)
            # a.num = num
            # a.save()
            post = m.DrugType.objects.filter(country_id=country_id, year=year, drug_id=drug_id)
            if not post:
                return "資料不存在，請重新輸入!"
            post.update(num=num)
        except m.DrugType.DoesNotExist:
            return False
        return True

    def createDrugTypeNum(**kwargs):
        drug_id = kwargs.get('drug_id')
        country_id = kwargs.get('country_id')
        year = kwargs.get('year')
        num = kwargs.get('num')
        try:
            ins = m.DrugType.objects.filter(country_id=country_id, year=year, drug_id=drug_id)
            if ins:
                return "資料已經存在，請重新輸入!"
            m.DrugType.objects.create(country_id=country_id, year=year, drug_id=drug_id, num=num)
            # ins.save()
        except Exception:
            return False
        return True

# 211226-001 刪除資料
class DelObject(models.Model):
    def delData(**kwargs):
        country_id = kwargs.get('country_id')
        year = kwargs.get('year')
        table = kwargs.get('table')
        tableObject = m.DrugCountry
        if table == "age_num":
            tableObject = m.DrugAge
        elif table == "gender_num":
            tableObject = m.DrugGender
        elif table == "drug_num":
            tableObject = m.DrugType
        item = tableObject.objects.filter(country_id=country_id, year=year)
        if item:
            item.delete()
        else:
            return False, "資料不存在"
        return True, ""