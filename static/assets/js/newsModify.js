newsdelete = function(parm){
    let data_id=parm.parentNode.getAttribute("newsid");
    let origin = parm.parentNode;
    Array.prototype.slice.call(origin.getElementsByTagName('button')).forEach(
        function(item) {
            item.remove();
        }
    );
    origin.innerHTML+='<ul class ="meta" id ="deleteline'+data_id+'"><li>確定要刪除嗎？</li><ul><button type="submit" onclick="deletedata()" style="margin-right: 3%;">確定</button><button type="submit" onclick="deletecancel()" style="margin-right: 3%;">取消</button></ul></ul>';
    

    deletecancel = function(){
        Array.prototype.slice.call(origin.getElementsByTagName('button')).forEach(
                function(item) {
                item.remove();
            });
            document.getElementById('deleteline'+data_id).remove();
            origin.innerHTML+='<button type="submit" class="modify" onclick = "newsput(this)" style="margin-right: 3%;">修改</button><button type="submit" onclick = "newsdelete(this)">刪除</button>'
    }
    
    deletedata = function(){
        let url = '/news/api/'+data_id;
        return fetch(url,{
            headers: {'user-agent': 'Mozilla/4.0 MDN Example','content-type': 'application/json'
            },
            method: 'DELETE'})
            .then(response => response.json())
            .then( window.location.reload())
    }
}

newsput = function(parm){
    let tputs = parm.parentNode.getElementsByTagName('h4')[0].innerText;
    let lputs = parm.parentNode.getElementsByTagName('a')[0].innerText;
    let origin = parm.parentNode;
    
    let data_id=parm.parentNode.getAttribute("newsid");
    parm.parentNode.innerHTML='<form method="put" action="" onsubmit="putdata(this); return false"><ul class="meta"><li><input size="70" type = "text" class="search" value="'+tputs+'" required></li></ul><ul><input size = "70" type = "text" class="search" value="'+lputs+'" required></ul> <button type="submit" style="margin-right: 3%;">確認</button><button onclick="cancel()">取消</button></form>'
    cancel = function(){
        origin.innerHTML='<ul class="meta"><li><h4>'+tputs+'</h4></li></ul><ul><a target="_blank" href="'+lputs+'">'+lputs+'</a></ul> <button type="submit" class="modify" onclick = "newsput(this)" style="margin-right: 3%;">修改</button><button type="submit" onclick = "newsdelete(this)">刪除</button>'
    }
    putdata = function(){
        
        const data = {'title':origin.getElementsByTagName('input')[0].value,'link':origin.getElementsByTagName('input')[1].value};
        const json = JSON.stringify(data);
        let url = '/news/api/'+data_id;
        
        fetch(url, {body: json,
            headers: {'user-agent': 'Mozilla/4.0 MDN Example','content-type': 'application/json'
            },
            method: 'PUT'})
            .then(function(response){
                if (response.status===400){
                    //alert來提醒
                    alert('偵測到網址或標題格式不符，請重新輸入')
                    
                    //origin.innerHTML+='<ul>輸入格式錯誤，請重新輸入</ul>';
                    
                }
                else{
                    window.location.reload()
                }
            })
    }
}

function addNews() {
    var title = document.getElementById("addTitle").value;
    var link = document.getElementById("addLink").value;
    var url = '/news/api/';
    fetch(url,
        {
            method:'POST',
            body:JSON.stringify({"title":title,"link":link}),
            headers:{'Content-Type':'application/json'}
        })
        .then(function(response){
            if (response.status===400){
                //alert來提醒
                alert('偵測到網址或標題格式不符，請重新輸入')
                //寫在網頁中，如果有用這個，在header中的ul的加入addnew
                
                //document.getElementById("addnew").innerHTML +="偵測到網址或標題格式不符，請重新輸入"

                
            }
            else{
                window.location.reload()
            }
        })
}


// 211224-001 爬蟲自動更新新聞資料
function autoUpdateNews() {
    spinner.removeAttribute('hidden');  // loading畫面
    var url = '/news/api/autoUpdateNews/';
    fetch(url,
        {
            method:'POST',
            headers:{'Content-Type':'application/json'}
        })
        .then(function(response){
            return response.json()
        }).then(function(myJson){
            if (!myJson['success']){
                //alert來提醒
                alert(myJson["desc"])
            }
            else{
                alert("新聞資料已自動更新")
                spinner.setAttribute('hidden', '');  // 解除loading
                window.location.reload()
            }
        })
}