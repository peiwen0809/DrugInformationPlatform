// t1：性別人數的表格，t2：年齡層人數的表格，t3：毒品種類的表格
// t1_tag[idx]為性別人數表格每一列的key，例：t1_tag1為男
// t1_value[idx]為性別人數表格每一列的人數，例：t1_value1為5260
// t1total為每一個表格的加總人數


// 新增欄位
function createCol() {
    getTabelCol("gender", "t1")  // 性別
    getTabelCol("age", "t2") // 年齡層
    getDrugList()  // 毒品種類
}

// 取得欄位
function getTabelCol(table, tableId) {
    var url = '/DIP/BaseTableSearch/getBaseTable/';
	fetch(url,
		{
			method:'POST',
			body:JSON.stringify({"table":table}),
			headers:{'Content-Type':'application/json'}
		})
	.then(function(response) {
		return response.json();
	})
	.then(function(myJson) {
		console.log(myJson)
        var data = myJson['data']
        displayNewCol(tableId, data)
	});
}

// 新增毒品種類欄位
function getDrugList() {
    var url = '/DIP/DrugIntro/showDrugList/';
	fetch(url,
		{
			method:'POST',
			body:JSON.stringify({"num":20,"start_id":1}),
			headers:{'Content-Type':'application/json'}
		})
	.then(function(response) {
		return response.json();
	})
	.then(function(myJson) {
		console.log(myJson)
        var data = myJson['data']
        displayNewCol('t3', data)
	});
}

// 呼叫完API後依序將欄位名稱放入表格
function displayNewCol(tableId, data) {
    var inner = document.getElementById(tableId);  // 要寫入的table
    // inner.innerHTML='';
    var label = "";
    if (tableId == "t1") {  // 性別
        label = 'gender';
    }else if (tableId == "t2") {  // 年齡層
        label = 'age_range';
    } else if (tableId == "t3") {  // 毒品種類
        label = "ch_name";
    } else {
        console.log("No define tableID")
        return
    }
    
    for (var i =0; i<data.length; i++){  // 在表格中依序顯示
        // 新增required必填，type改為數字，避免被輸入非數字、小數，限定最小值為0
        var addhtml = '<tr><td align="center" id='+tableId+'_tag'+i+'>'+data[i][label]+'</td><td align="center"><input type="number" min="0" class="addsearch1" id='+tableId+'_value'+i+' value="0" required></td></tr>'
        inner.innerHTML+=addhtml;
    }
    // 最後一列的合計值為0
    var totalHtml = '<tr><td></td></tr><tr><td align="center">合計</td><td id='+tableId+'total align="center">0</td></tr>'
    inner.innerHTML+=totalHtml;
}

// 新增前要先檢查這個年份是否已經存在
function add() {
    var id = 0;
	if (sessionStorage.getItem("country_id") != null) {
		id = sessionStorage.getItem("country_id");
	}
    var url = '/DIP/DrugSearch/getCountryYearNum/';
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
        var year = document.getElementById('yearBox').value;  // 當前年份
        var param = myJson['data'];  // 取出data的array
        // 檢查這個年份是不是已經存在
        for (var i = 0; i < param.length; i++) {
            if (param[i]['year'] == year){
                alert("新增失敗，"+year+"年的資料已經存在，請重新輸入")
                return
            }
        }
        modify()  // 呼叫updatecase.js 的方法
    });
}