var drugList = []
// 呼叫api，取得毒品種類清單
function getDrugList() {
	var url = '/DIP/DrugIntro/showDrugList/';
	fetch(url,
		{
			method:'POST',
			body:JSON.stringify({"start_id":0, num:13}),  // 最後一筆為其他，不需要取出來
			headers:{'Content-Type':'application/json'}
		})
	.then(function(response) {
		return response.json();
	})
	.then(function(myJson) {
		console.log(myJson)
        var data = myJson['data']
		drugList = data
        var imgPath = document.getElementById('drugImg').src  // 取得圖片根目錄
        var drugContent = document.getElementById('drugContent')  // 顯示的區塊
		drugContent.innerHTML = ""
        for (var i=0;i<data.length;i++) {
            drugContent.innerHTML += '<li><article class="box post-summary"><h3><a href="#" onclick="showDrugView('+i+')">'+data[i]['ch_name']+'</a></h3><ul class="meta"><li><img class="drugimage" id="drug'+data[i]['drug_id']+'"></li></ul><ul><li><p>'+data[i]['drug_intro']+'</p></li></ul></article></li>'
            var imgId = document.getElementById("drug"+i)  // 毒品圖片的區塊，根據資料庫中指定的圖片名稱替換
            // console.log(imgPath)
            var lastidx = imgPath.lastIndexOf("/");  //最後一個斜線後為圖片名稱，要換成別的圖片
            imgId.src = imgPath.substr(0,lastidx+1) + data[i]['img1']+".jpg";
        }
	});
}

// 點毒品名稱跳轉到毒品詳細介紹
function showDrugView(id) {
    location.href="/Druginfoview/"
	sessionStorage.setItem("drug",id)  // 將毒品id放到session，讓跳轉到詳細資料的頁面時可以知道是哪個毒品
}

function showInfo() {
    var url = '/DIP/DrugIntro/getDrugInfo/';
	var drug_id = sessionStorage.getItem('drug')
	fetch(url,
		{
			method:'POST',
			body:JSON.stringify({"id":drug_id}),
			headers:{'Content-Type':'application/json'}
		})
	.then(function(response) {
		return response.json();
	})
	.then(function(myJson) {
		console.log(myJson)
		var druginfoview = document.getElementById('druginfoview')
		druginfoview.innerHTML += '<h4>'+myJson['ch_name']+'</h4><section><span><img class="drugimage" id="img1"></span><span ><img class="drugimage" id="img2"></span><span ><img class="drugimage" id="img3"></span></section><section><p>'+myJson['drug_intro']+'</p></section>'
        
		var imgPath = document.getElementById('drugImg').src
		// console.log(imgPath)
		for (var i=1;i<=3;i++) {  // 一共會顯示三張圖片
			var imgseq = document.getElementById("img"+i)
			var lastidx = imgPath.lastIndexOf("/");  //最後一個斜線後為圖片名稱，要換成別的圖片
			imgseq.src = imgPath.substr(0,lastidx+1) + myJson['img'+i]+".jpg";
		}
	});
}


function doSearch() {
	// console.log(document.getElementById('searchDrug').value)
	var keyword = document.getElementById('searchDrug').value
	var result = []
	for (var i=0; i<drugList.length; i++) {
		var str = JSON.stringify(drugList[i])
		if (str.includes(keyword)) {
			result.push(drugList[i])
		}
	}

	var imgPath = document.getElementById('drugImg').src  // 取得圖片根目錄
	var drugContent = document.getElementById('drugContent')  // 顯示的區塊
	drugContent.innerHTML = ""
	for (var i=0;i<result.length;i++) {
		drugContent.innerHTML += '<li><article class="box post-summary"><h3><a href="#" onclick="showDrugView('+i+')">'+result[i]['ch_name']+'</a></h3><ul class="meta"><li><img class="drugimage" id="drug'+result[i]['drug_id']+'"></li></ul><ul><li><p>'+result[i]['drug_intro']+'</p></li></ul></article></li>'
		var imgId = document.getElementById("drug"+result[i]['drug_id'])  // 毒品圖片的區塊，根據資料庫中指定的圖片名稱替換
		// console.log(imgPath)
		var lastidx = imgPath.lastIndexOf("/");  //最後一個斜線後為圖片名稱，要換成別的圖片
		imgId.src = imgPath.substr(0,lastidx+1) + result[i]['img1']+".jpg";
	}

	console.log(result)
}