from django.db import models

from django.utils import timezone

class NewsList(models.Model):
  title=models.CharField(max_length=200)
  link=models.URLField(max_length=200)
  def __str__(self):
    return self.Newstitle

  class Meta:
    db_table = "news"  # 211208-001 指定table名稱，不然預設會是APP name_model name