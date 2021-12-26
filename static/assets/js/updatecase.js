// t1：性別人數的表格，t2：年齡層人數的表格，t3：毒品種類的表格
// t1_tag[idx]為性別人數表格每一列的key，例：t1_tag1為男
// t1_value[idx]為性別人數表格每一列的人數，例：t1_value1為5260
// t2_id[idx]為年齡層人數表格性別在資料庫裡的id，例：t2_id1為14
// t1total為每一個表格的加總人數


// {"data":[{"year":"2020","num":10000},{"year":"2019","num":20000},...]}
// 呼叫api，傳入方法名稱，取年份
function getCountryYears(name) {
    document.getElementById('selectBox').value = sessionStorage.getItem("country_id");
	var id = 0;
	if (sessionStorage.getItem("country_id") != null) {
		id = sessionStorage.getItem("country_id");
	}
	var url = '/DIP/DrugSearch/' + name + '/';
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
        var numArr = [];  //查詢國家年份總人數
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
    var url = '/DIP/DrugSearch/' + name + '/';
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
        var idArr = [];  // 資料庫中的id [0,2,5,9...]
        var param = myJson['data'];  // 取出data的array
        for (var i = 0; i < param.length; i++) {
            if (param[i]['year'] == value) {
                labelArr.push(param[i][label])
                numArr.push(param[i]['num'])
                idArr.push(param[i][label+"_id"])  // 211222-001 新增一欄ID，為tag在資料庫裡的ID，為了更新的時候可以指定要修改哪一筆資料
            }
        }
        display(tableId,labelArr,numArr,idArr)
        console.log(myJson)
    });
}


// 得到回傳值後顯示在頁面上
function display(tableId,labelArr,numArr,idArr) {
    var inner = document.getElementById(tableId);  // 要寫入的table
    inner.innerHTML='';
    
    var total = 0;  // 人數合計
    for (var i =0; i<labelArr.length; i++){  // 在表格中依序顯示
        // 新增required必填，type改為數字，避免被輸入非數字、小數，限定最小值為0
        // 211222-001 新增一欄ID，為tag在資料庫裡的ID，為了更新的時候可以指定要修改哪一筆資料，不顯示
        var addhtml = '<tr><td align="center" style="display: none;" id='+tableId+'_id'+i+'>'+idArr[i]+'</td><td align="center" id='+tableId+'_tag'+i+'>'+labelArr[i]+'</td><td align="center"><input type="number"  min="0" class="addsearch1" value='+numArr[i]+' id='+tableId+'_value'+i+' required></td></tr>'
        inner.innerHTML+=addhtml;
        total = total+numArr[i];
    }
    // 最後一列的合計值
    var totalHtml = '<tr><td align="center">合計</td><td id='+tableId+'total align="center">'+total+'</td></tr>'
    inner.innerHTML+=totalHtml;

    // 將table資料筆數存在公共變數
    // 因為每次改年份要重新抓人數資料，會將表格所有資料清除，所以要重新補上表頭
    if (tableId == 't1') {
        inner.innerHTML = '<th align="center">性別</th><th align="center">人數</th>' + inner.innerHTML
        // genderCount = labelArr.length;
    } else if (tableId == 't2') {
        inner.innerHTML = '<th align="center">年齡層</th><th align="center">人數</th>' + inner.innerHTML
        // ageCount = labelArr.length;
    } else {
        inner.innerHTML = '<th align="center">毒品</th><th align="center">人數</th>' + inner.innerHTML
        // typeCount = labelArr.length;
    }
}


// {"country_id":1,"year":"2020","num":20000}
// {"country_id":1,"year":"2020","data":[{"age_id":1,"num":20000},{"age_id":2,"num":20000},{...}]}
// {"country_id": 1, "year": "2020", "num": 400000, "data_age": [{"age_id": 1, "num": 20000}, {"age_id": 2, "num": 20000}, {...}], "data_gender": [{"gender": "male", "num": 20000}, {"gender": "female", "num": 20000}], # "data_drug": [{"drug_id": 1, "num": 20000}, {"drug_id": 2, "num": 20000}, {...}]}
// 呼叫修改人數的API
function modify() {
    var totalNum = sumTotal()  // 檢查人數
    if (totalNum != -1) {  // -1表示人數加總不相同，所以不更新
        spinner.removeAttribute('hidden');  // loading畫面
        modifyData("CountryYearNum", totalNum)  // 更新總人數
        modifyData("GenderNum", totalNum)  // 更新性別人數
        modifyData("AgeNum", totalNum)  // 更新年齡層人數
        modifyData("DrugTypeNum", totalNum)  // 更新毒品種類人數
    }
}

// 加總人數並檢查年齡層與性別加總的人數是否相同
function sumTotal() {
    var genderTotal = 0;
    var ageTotal = 0;
    var typeTotal = 0;
    // 加總性別總人數
    var genderCount = document.getElementById('t1').getElementsByTagName('tr').length - 2;
    for (var i=0;i<genderCount;i++) {
        genderTotal += parseInt(document.getElementById('t1_value'+i).value);
    }
    // 加總年齡層總人數
    var ageCount = document.getElementById('t2').getElementsByTagName('tr').length - 2;
    for (var i=0;i<ageCount;i++) {
        ageTotal += parseInt(document.getElementById('t2_value'+i).value);
    }
    // 加總毒品種類總人數
    var typeCount = document.getElementById('t3').getElementsByTagName('tr').length - 2;
    for (var i=0;i<typeCount;i++) {
        typeTotal += parseInt(document.getElementById('t3_value'+i).value);
    }
    // console.log(genderTotal,ageTotal,typeTotal)
    // 更新顯示合計值
    document.getElementById('t1total').innerHTML = genderTotal;
    document.getElementById('t2total').innerHTML = ageTotal;
    document.getElementById('t3total').innerHTML = typeTotal;
    if (genderTotal != ageTotal) {
        alert("性別人數與年齡層人數加總不相等")
        return -1;
    }else {
        return genderTotal;
    }
}

var successCnt = 0
// 呼叫更新API
function modifyData(name, total) {
    try {
        var label = "";  // JSON的key不同，所以根據要傳的方法辨別
        var tableId = "";  // 是在哪一張表
        var alertDesc = ""
        if (name == "GenderNum") {  // 性別
            label = "gender_id";
            tableId = 't1';
            alertDesc = "性別人數";
        } else if (name == "AgeNum") {  //年齡層
            label = "age_id";
            tableId = 't2';
            alertDesc = "年齡層人數";
        } else if (name == "DrugTypeNum") {  // 毒品種類
            label = "drug_id";
            tableId = 't3';
            alertDesc = "毒品種類人數";
        } else {
            label = ""
            alertDesc = "總人數";
        }
        var country_id = sessionStorage.getItem("country_id");  // 當前國家ID
        var year = document.getElementById('yearBox').value;  // 當前年份
        
        var requestJson = {}  // 請求的Json格式
        var data = [];
        if (label != "") {
            var count = document.getElementById(tableId).getElementsByTagName('tr').length - 2;  // 總共有幾筆資料要更新，要扣掉第一欄跟最後一欄合計
            for (var i=0;i<count;i++) {
                var d = {};
                d[label] = document.getElementById(tableId+'_id'+i).innerText;
                d['num'] = document.getElementById(tableId+'_value'+i).value;
                data.push(d)
            }
            requestJson = {"country_id":country_id, "year":year, "data":data}
        }else {  // 總人數
            requestJson = {"country_id":country_id, "year":year, "num":total}
        }
        console.log(requestJson)

        
        if (document.getElementById('addcase') != null){
            name = "insert"+name;
        }else {
            name = "get"+name;
        }
        var url = "/DIP/SearchManage/" + name + "/"
        fetch(url,
        	{
        		method:'POST',
        		body:JSON.stringify(requestJson),
        		headers:{'Content-Type':'application/json'}
        	})
        .then(function(response) {
        	return response.json();
        })
        .then(function(myJson) {
            console.log(myJson)
            if (myJson['success']) {
                successCnt++;
                // 判斷是否四個表都新增成功
                if (successCnt == 4) {
                    alert("新增/更新 成功!")
                    successCnt = 0;
                    window.location.reload()
                    spinner.setAttribute('hidden', '');  // 解除loading
                }
            }else {
                alert(alertDesc+"新增/修改失敗，失敗描述："+myJson['desc'])
                successCnt = 0;
                window.location.reload()
                spinner.setAttribute('hidden', '');  // 解除loading
            }
        });
    }catch(e) {
        console.log(e)
        
    }
}

const spinner = document.getElementById("spinner");
function delData(){
    var country_id = sessionStorage.getItem('country_id')
    var year = document.getElementById('yearBox').value
    var dialog = confirm("確定要刪除"+year+"年的資料? 刪除後無法復原");
    if (dialog) {
        spinner.removeAttribute('hidden');  // loading畫面
        var requestJson = {"country_id":country_id, "year":year}
        var url = "/DIP/SearchManage/delCountryYearData/"
            fetch(url,
                {
                    method:'POST',
                    body:JSON.stringify(requestJson),
                    headers:{'Content-Type':'application/json'}
                })
            .then(function(response) {
                return response.json();
            })
            .then(function(myJson) {
                console.log(myJson)
                if (myJson['success']) {
                    alert("刪除成功!")
                }else {
                    alert("刪除失敗，失敗描述："+myJson['desc'])
                }
                spinner.setAttribute('hidden', '');  // 解除loading
                window.location.reload()
            });
    }
}