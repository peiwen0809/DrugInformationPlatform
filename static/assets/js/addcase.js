
// 載入這個國家有資料的年份
function onloadYear(yearArr){ 
    document.getElementById("yearBox").innerHTML = "";  // 清空年份的下拉式選單
    var select = document.getElementById("yearBox");   // 取得年份的下拉式選單
    for(var x=0;x<yearArr.length;x++){  // 根據傳入的年份陣列建立下拉式選單
        var option = document.createElement("option"); 
        option.setAttribute("value",yearArr[x]);
        option.appendChild(document.createTextNode(yearArr[x])); 
        select.appendChild(option);
    }
    select.value = yearArr[yearArr.length-1];   // 預設為最新的年份
  } 

  // {"data":[{"year":"2020","num":10000},{"year":"2019","num":20000},...]}
  // 呼叫api，傳入方法名稱，取年份
function getCountryYears(name) {
    document.getElementById('selectBox').value = sessionStorage.getItem("country_id");
	var id = 0;
	if (sessionStorage.getItem("country_id") != null) {
		id = sessionStorage.getItem("country_id");
	}
	var url = 'http://127.0.0.1:8000/DIP/DrugSearch/' + name + '/';
	fetch(url,
		{
			method:'POST',
			body:JSON.stringify({"id":id}),
			headers:{'Content-Type':'application/json'}
		})
	.then(function(response) {
		return response.json();
	})
	.then(function(myJson) {
        var param = myJson['data'];  // 取出data的array
        var numArr = [];  //如果是查詢國家年份總人數的話，只會有一條折線，json格式跟其他三個不同，所以要另外處理
        var yearArr = [];  //存放年份
        for (var i = 0; i < param.length; i++) {
            yearArr.push(param[i]['year']);
            numArr.push(param[i]['num']);
        }
        dataSet = {"總人數":{"num": numArr, "year": yearArr}};
        onloadYear(yearArr)
        totalTable(yearArr[yearArr.length-1])
		console.log(myJson)
	});
}

// 抓年齡層、性別、毒品種類的資料
function totalTable(value) {
    getRowData('getAgeNum',value)
    getRowData('getGenderNum',value)
    getRowData('getDrugTypeNum',value)
}

// {"data":[{"year":"2020","num":5000,"age":"0-20"},{"year":"2020","num":1000,"age":"21-30"},...]}
// 呼叫api，傳入方法名稱及年份，取年齡、性別、毒品種類的資料
function getRowData(name,value) {
    var id = 0;
    if (sessionStorage.getItem("country_id") != null) {
        id = sessionStorage.getItem("country_id");
    }
    var url = 'http://127.0.0.1:8000/DIP/DrugSearch/' + name + '/';
    fetch(url,
        {
            method:'POST',
            body:JSON.stringify({"id":id}),
            headers:{'Content-Type':'application/json'}
        })
    .then(function(response) {
        return response.json();
    })
    .then(function(myJson) {
        // 查詢不同的資料會有不同的欄位名稱
        var label = '';
        var tableId = '';
        switch (name) {
            case 'getAgeNum':  //年齡層
                label = 'age';
                tableId = 't2';
                break;
            case 'getGenderNum':  // 性別
                label = 'gender';
                tableId = 't1';
                break;
            case 'getDrugTypeNum':  // 毒品種類
                label = 'type';
                tableId = 't3';
                break;
            default:
                console.log("Not define")
        }

        
        var labelArr = [];  // ["0-19","20-29"...] OR ["男","女"] OR ["大麻","海洛因"...]
        var numArr = [];  // [200,300,100...]
        var param = myJson['data'];  // 取出data的array
        for (var i = 0; i < param.length; i++) {
            if (param[i]['year'] == value) {
                labelArr.push(param[i][label])
                numArr.push(param[i]['num'])
            }
        }
        display(tableId,labelArr,numArr)
        console.log(myJson)
    });
}


var genderCount = 0;
var ageCount = 0;
var typeCount = 0;
// 得到回傳值後顯示在頁面上
function display(tableId,labelArr,numArr) {
    var inner = document.getElementById(tableId);  // 要寫入的table
    inner.innerHTML='';
    
    var total = 0;  // 人數合計
    for (var i =0; i<labelArr.length; i++){  // 在表格中依序顯示
        var addhtml = '<tr><td align="center">'+labelArr[i]+'</td><td align="center"><input type="text" class="addsearch1" value='+numArr[i]+' id='+tableId+i+'></td></tr>'
        inner.innerHTML+=addhtml;
        total = total+numArr[i];
    }
    var totalHtml = '<tr></tr><tr><td align="center">合計：</td><td id='+tableId+'total align="center">'+total+'</td></tr>'
    inner.innerHTML+=totalHtml;

    // 將table資料數存在公共變數
    if (tableId == 't1') {
        inner.innerHTML = '<th align="center">性別</th><th align="center">人數</th>' + inner.innerHTML
        genderCount = labelArr.length;
    } else if (tableId == 't2') {
        inner.innerHTML = '<th align="center">年齡層</th><th align="center">人數</th>' + inner.innerHTML
        ageCount = labelArr.length;
    } else {
        inner.innerHTML = '<th align="center">毒品</th><th align="center">人數</th>' + inner.innerHTML
        typeCount = labelArr.length;
    }
}

// 加總人數比對，三個人數要相同
function sumTotal() {
    var genderTotal = 0;
    var ageTotal = 0;
    var typeTotal = 0;
    // 加總性別總人數
    for (var i=0;i<genderCount;i++) {
        genderTotal += parseInt(document.getElementById('t1'+i).value);
    }
    // 加總年齡層總人數
    for (var i=0;i<ageCount;i++) {
        ageTotal += parseInt(document.getElementById('t2'+i).value);
    }
    // 加總毒品種類總人數
    for (var i=0;i<typeCount;i++) {
        typeTotal += parseInt(document.getElementById('t3'+i).value);
    }
    console.log(genderTotal,ageTotal,typeTotal)
    // 更新顯示合計值
    document.getElementById('t1total').innerHTML = genderTotal;
    document.getElementById('t2total').innerHTML = ageTotal;
    document.getElementById('t3total').innerHTML = typeTotal;
    if (genderTotal != ageTotal || ageTotal != typeTotal || genderTotal != typeTotal) {
        alert("三個類別人數加總不相等")
    }
}

// {"country_id": 1, "year": "2020", "num": 400000, "data_age": [{"age_id": 1, "num": 20000}, {"age_id": 2, "num": 20000}, {...}], "data_gender": [{"gender": "male", "num": 20000}, {"gender": "female", "num": 20000}], # "data_drug": [{"drug_id": 1, "num": 20000}, {"drug_id": 2, "num": 20000}, {...}]}
// 呼叫修改人數的API
function modify() {
    sumTotal()
    // 呼叫API
}



