from django.db import models

from django.utils import timezone

class NewsList(models.Model):
  title=models.CharField(max_length=200)
  link=models.URLField(max_length=200)
  def __str__(self):
    return self.title

  class Meta:
    db_table = "news"  # 211208-001 指定table名稱，不然預設會是APP name_model name


# 211224-001 新增爬蟲抓取新聞標題、連結，並寫入資料庫
import urllib.request as req
import sqlite3
def autoUpdate():
  src = "https://udn.com/search/tagging/2/%E6%AF%92%E5%93%81"
  request = req.Request(src, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
  })  # 建立一Request物件，附加Headers的資訊來模仿使用者連線的機制
  with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
  # print(data)
  import bs4
  root = bs4.BeautifulSoup(data, "html.parser")  # 以beautifulsoup4來協助HTML格式的解析

  titles = root.find_all("div", class_="story-list__text")  # 尋找div中，子標籤為"story-list__text"的內容

  con = sqlite3.connect('drugcase.db')  # 連線到資料庫

  cur = con.cursor()  # 建立cursor物件，為編輯資料庫物件

  dbnews = cur.execute("SELECT link FROM news;")
  dbnewsitem = []
  dbnewsitem = dbnews.fetchall()

  item = cur.execute("SELECT COUNT(id) FROM news;")
  itemcount = item.fetchall()[0]  # itenount為資料庫中news的筆數

  for titlename in titles:  # 把tiltles中的資料一筆一筆抓出來
    if titlename.h2 != None:  # 若新聞未被刪除
      count = 0  # 計算是否為迴圈的最後一筆新聞
      for (news,) in dbnewsitem:
        if titlename.select_one("a").get("href") == news:  # 若抓下來的該筆link存在於資料庫中
          count += 1
          break
        else:
          count += 1
          if count == itemcount[0]:  # 如果找完資料庫中裡所有連結了但仍未找到資料庫中有此link
            cur.execute("""INSERT INTO news (title, link) 
                      VALUES (?,?)""", (titlename.h2.text, titlename.select_one("a").get("href"),))
            break
          continue

  con.commit()  # 確認並寫入資料庫

  con.close()
