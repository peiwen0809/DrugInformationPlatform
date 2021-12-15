from django.db import models


# Create your models here.
class Admin(models.Model):
    account = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.account  # 顯示帳號

    class Meta:
        db_table = 'admin'
