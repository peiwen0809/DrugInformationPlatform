// 呼叫登入的API
function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var url = 'http://127.0.0.1:8000/DIP/login/login/';
	fetch(url,
		{
			method:'POST',
			body:JSON.stringify({"account":username, "password":password}),
			headers:{'Content-Type':'application/json'}
		})
	.then(function(response) {
		return response.json();
	})
	.then(function(myJson) {
        checkAuth(username,myJson)
		
	});
}

// {"success":True/False, "desc":"帳號/密碼錯誤"}
// 判斷是否登入成功
function checkAuth(username,myJson) {
    if (myJson['desc'] == 'Successful') {  //登入成功回到上一頁
        history.back();
    } else {
        alert(myJson['desc'])
    }
    sessionStorage.setItem("user", username);  //儲存session

    console.log(myJson)
}