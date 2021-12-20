// 畫圖元件
var ctx = document.getElementById("chart-area");  // 對應到html的canvas id
var c = ctx.getContext('2d');
c.clearRect(0, 0, ctx.width, ctx.height);
var myChart = new Chart(ctx,{});

// 呼叫api，傳入方法名稱及國家ID
function callApi(name) {
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
		drawChart(name, myJson)  // 畫圖
	});
}

// {"data":[{"year":"2020","num":10000},{"year":"2019","num":20000},...]}
// {"data":[{"year":"2020","num":5000,"age":"0-20"},{"year":"2020","num":1000,"age":"21-30"},...]}
// 畫折線圖
function drawChart(name, myJson) {
	// 查詢不同的資料會有不同的欄位名稱
	var label = '';
	switch (name) {
		case 'getAgeNum':  //年齡層
			label = 'age';
			break;
		case 'getGenderNum':  // 性別
			label = 'gender';
			break;
		case 'getDrugTypeNum':  // 毒品種類
			label = 'type';
			break;
		case 'getCountryYearNum':  //每年總人數
			label = 'all';
			break;
		default:
			console.log("Not define")
	}

	var param = myJson['data'];  // 取出data的array
	var chartArr = [];  // 如果是年齡層、性別、毒品種類會有多條折線，要依序放入這個array
	var dataSet = {};  // 每一個年齡層(性別、毒品種類)會有各自的資料，要取出整理。例：{"0-19":{"num":[123,456],"year":[2019,2020]},"20-29":{"num":[123,456],"year":[2019,2020]},...}
	
	var numArr = [];  //如果是查詢國家年份總人數的話，只會有一條折線，json格式跟其他三個不同，所以要另外處理
	var yearArr = [];  //存放年份
	if (label == 'all') {  //國家總人數
		for (var i = 0; i < param.length; i++) {
			yearArr.push(param[i]['year']);
			numArr.push(param[i]['num']);
		}
		dataSet = {"總人數":{"num": numArr, "year": yearArr}};
	} else {  //年齡層、性別、毒品種類
		for (var i = 0; i < param.length; i++) {
			yearArr.push(param[i]['year'])
			if (param[i][label] in dataSet) {  // 如果已經有資料了，將資料加入原本的array
				var tmp = dataSet[param[i][label]];
				var numTmp = tmp['num'];
				numTmp.push(param[i]['num']);
				var yearTmp = tmp['year'];
				yearTmp.push(param[i]['year']);
				dataSet[param[i][label]] = {"num":numTmp, "year":yearTmp};
			}else {
				dataSet[param[i][label]] = {"num":[param[i]['num']], "year":[[param[i]['year']]]};
			}
		}
	}
	yearArr = [...new Set(yearArr)];  //去除年份的重複
	
	// 組成繪圖資料
	for (var key in dataSet){
		// 折線顏色隨機
		var r = Math.floor(Math.random() * 255);
		var g = Math.floor(Math.random() * 255);
		var b = Math.floor(Math.random() * 255);
		var color = 'rgb(' + r + ', ' + g + ', ' + b + ')';

		var chartData = {
			label: key, //標籤
			data: dataSet[key]['num'], //資料
			borderColor: color,
			backgroundColor: color,
			//外框線寬度
			borderWidth: 1
		};
		chartArr.push(chartData);
	}

	myChart.destroy();
	//標籤若超過兩個要用陣列表示，若沒有就是字串表示
	myChart = new Chart(ctx, {
		type: "line", //圖表類型，折線圖
		data: {
			labels: yearArr,  // y軸標籤
			datasets: chartArr
		},
		options: {
			scales: {
				x: {
					title: {
						display: true,
						text: '年'
					}
				},
				y: {
					title: {
						display: true,
						text: '人數'
					}
				}
			}
		}
	});
	console.log(myJson);
}

