// 顯示登入資訊
// 登入登出共用同一個物件
if (sessionStorage.getItem("user") != null) {
    document.getElementById('loginSession').innerHTML=sessionStorage.getItem("user")+" 您好"
    document.getElementById('loginSts').innerHTML="登出"
}else {
    document.getElementById('loginSts').innerHTML="登入"
}
if (sessionStorage.getItem("country_id") == null) {
    sessionStorage.setItem("country_id",0);  // 指定一開始的國家
}


//根據在首頁點選的國家更改統計資料查詢下拉選單的預設選項
function loadSelectedCountry() {
    document.getElementById('selectBox').value = sessionStorage.getItem("country_id");
    if (document.getElementById("countryImg") != null) {
        changeImg()
    }
    
}

// 根據下拉式選單選的國家，更改國家圖片及重新呼叫總人數的API
function changeImg() {
    var imgPath = document.getElementById("countryImg");  // 取得圖片位址
    var img = "tw.png";
    if (sessionStorage.getItem("country_id") == "1") {  // 新加坡
        img = "sin.png";
    }else if (sessionStorage.getItem("country_id") == "2") {  // 馬來西亞
        img = "ma.png";
    }
    console.log(imgPath.src)
    var imgRoot = imgPath.src;
    var lastidx = imgRoot.lastIndexOf("/");  //最後一個斜線後為圖片名稱，要換成別的圖片
    imgPath.src = imgRoot.substr(0,lastidx+1) + img;
    callApi('getCountryYearNum')
}


// 如果目前為登入狀態，則清除session，否則跳轉到登入頁面
function logInOut() {
    if (sessionStorage.getItem("user") != null) {
        sessionStorage.removeItem("user")
        // location.reload()
        location.href="/"  // 如果登出跳回首頁
    }else {
        location.href="/login/"
    }
}

//TODO 有沒有不需要寫死路徑的方法?
//檢查是否登入
function jumpToNews(){
    if (sessionStorage.getItem("user") != null) {
        location.href="/news/Mgrnewsview/"
    }else {
        alert("此功能僅限管理者使用，請先登入")
    }
}
//TODO 有沒有不需要寫死路徑的方法?
//檢查是否登入
function jumpToSearch(){
    // console.log(document.getElementById("search").getAttribute("href"))
    if (sessionStorage.getItem("user") != null) {
        location.href="/Mgrsearchview/"
    }else {
        alert("此功能僅限管理者使用，請先登入")
    }
}

// 將國家ID存在session，跟後端要資料時需要用到國家ID
function setCountrySession(id) {
    sessionStorage.setItem("country_id",id)
}