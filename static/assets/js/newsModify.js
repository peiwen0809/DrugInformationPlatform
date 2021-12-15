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
    parm.parentNode.innerHTML='<ul class="meta"><li><input size="70" type = "text" class="search" value="'+tputs+'"></li></ul><ul><input size = "70" type = "text" class="search" value="'+lputs+'"></ul> <button type="submit" onclick="putdata()" style="margin-right: 3%;">確認</button><button onclick="cancel()" type="submit">取消</button>'
    cancel = function(){
        origin.innerHTML='<ul class="meta"><li><h4>'+tputs+'</h4></li></ul><ul><a target="_blank" href="'+lputs+'">'+lputs+'</a></ul> <button type="submit" class="modify" onclick = "newsput(this)" style="margin-right: 3%;">修改</button><button type="submit" onclick = "newsdelete(this)">刪除</button>'
    }
    putdata = function(){
        
        const data = {'title':origin.getElementsByTagName('input')[0].value,'link':origin.getElementsByTagName('input')[1].value};
        const json = JSON.stringify(data);
        let url = '/news/api/'+data_id;
        
        return fetch(url, {body: json,
            headers: {'user-agent': 'Mozilla/4.0 MDN Example','content-type': 'application/json'
            },
            method: 'PUT'})
            .then(response => response.json())
            .then( window.location.reload())
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
    .then(response => response.json())
    .then( window.location.reload());

}