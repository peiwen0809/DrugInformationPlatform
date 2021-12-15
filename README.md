# SE_final

首頁：127.0.0.1:8000

## DrugNews 新聞模組
### 取得新聞列表(GET)
http://localhost:8000/news/api/
### 插入新聞(POST)
http://localhost:8000/news/api/
- title：新聞標題
- link：新聞連結
```Json
{"title":"test25","link":"https://google.com"}
```
```Json
[
    {
        "id": 2,
        "title": "測試2",
        "link": "http://123456.222"
    },
    {
        "id": 1,
        "title": "測試",
        "link": "http://...."
    }
]
```
### 更新新聞(PUT)
http://localhost:8000/news/api/{id}
```
http://localhost:8000/news/api/4
```
```Json
{"id":5,"title":"test26","link":"https://google.com"}
```
### 刪除新聞(DEL)
http://localhost:8000/news/api/{id}
```
http://localhost:8000/news/api/4
```

## DrugSearch 搜尋管理模組
### 查詢國家每年吸毒人口
http://127.0.0.1:8000/DIP/DrugSearch/getCountryYearNum/
```Json
{"id":1}
```
```Json
{"id": 1, "img": "D:/Users/User/Desktop/SE_IMG/country_year_num.png"}
```
### 查詢國家每年吸毒人口，依性別區分
http://127.0.0.1:8000/DIP/DrugSearch/getGenderNum/
```Json
{"id":1}
```
```Json
{"id": 1, "img": "D:/Users/User/Desktop/SE_IMG/gender_num.png"}
```
### 查詢國家每年吸毒人口，依年齡層區分
http://127.0.0.1:8000/DIP/DrugSearch/getGenderNum/
```Json
{"id":1}
```
```Json
{"id": 1, "img": "D:/Users/User/Desktop/SE_IMG/age_num.png"}
```
### 查詢國家每年吸毒人口，依毒品種類區分
http://127.0.0.1:8000/DIP/DrugSearch/getGenderNum/
```Json
{"id":1}
```
```Json
{"id": 1, "img": "D:/Users/User/Desktop/SE_IMG/drug_type_num.png"}
```
