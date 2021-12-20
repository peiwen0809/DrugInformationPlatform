window.onload = () =>{
    getcontent()
}

// 從DB抓新聞資料
const getcontent = () =>{
    fetch('/news/api')
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    //分頁
    jsonData = data;
    pagination(jsonData,1)
  });
}
  
const pageid = document.getElementById('pageid');
let jsonData = {};

// 分頁
function pagination(data, nowPage) {
    // 取得全部資料長度
    const dataTotal = data.length;

    // 要顯示在畫面上的資料數量，預設每一頁只顯示五筆資料。
    const perpage = 10;

    // page 按鈕總數量公式 總資料數量 / 每一頁要顯示的資料
    // 這邊要注意，因為有可能會出現餘數，所以要無條件進位。
    const pageTotal = Math.ceil(dataTotal / perpage);
    console.log(`全部資料:${dataTotal} 每一頁顯示:${perpage}筆 總頁數:${pageTotal}`);

    // 當前頁數
    let currentPage = nowPage;  

    // 當"當前頁數"比"總頁數"大的時候，"當前頁數"就等於"總頁數"
    if (currentPage > pageTotal) {
        currentPage = pageTotal;
    }
    const minData = (currentPage * perpage) - perpage;
    const maxData = (currentPage * perpage) -1;
    const newdata = [];

    for (var i=0;i<dataTotal;i++) {
        if ( i >= minData && i <= maxData) {
            newdata.push(data[i]);
        }
    }
    // console.log(newdata)
    // 用物件方式來傳遞資料
    const page = {
        pageTotal,  // 總頁數
        currentPage,  // 當前頁數
        hasPage: currentPage > 1,  // 是否有前一頁
        hasNext: currentPage < pageTotal,  // 是否有下一頁
    }
    // 印出一頁的內容
    let inner = document.getElementById('context');
    inner.innerHTML=''
    var context = document.getElementById("context")
    if (context.dataset.idf == "Mgrnewsview") {
        for (let i =0; i<newdata.length; i++){
            let addhtml='<article class="box post-summary" newsid ='+newdata[i]['id']+'><ul class="meta"><li><h4 >'+newdata[i]['title']+'</h4></li></ul><ul><a target="_blank" href="'+newdata[i]['link']+'">'+newdata[i]['link']+'</a></ul> <button type="submit" class="modify" onclick = "newsput(this)" style="margin-right: 3%;">修改</button><button type="submit" onclick = "newsdelete(this)">刪除</button></article>'
            inner.innerHTML+=addhtml;
        }
    } else {
        for (let i =0; i<newdata.length; i++){
            let addhtml='<article class="box post-summary" newsid ='+newdata[i]['id']+'><ul class="meta"><li><h4>'+newdata[i]['title']+'</h4></li></ul><ul><a target="_blank" href="'+newdata[i]['link']+'">'+newdata[i]['link']+'</a></ul></article>'
            inner.innerHTML+=addhtml;
        }
    }
    
    pageBtn(page);  // 換頁按鈕
}
// 換頁按鈕
function pageBtn (page){
    let str = '';
    const total = page.pageTotal;

    if(page.hasPage) {
        // str += `<li class="page-item"><a class="page-link" href="#" data-page="${Number(page.currentPage) - 1}">上一頁</a></li>`;
        str += `<li><a href="#" data-page="${Number(page.currentPage) - 1}">上一頁</a></li>`;
    } else {
        // str += `<li class="page-item disabled"><span class="page-link">上一頁</span></li>`;
        str += `<li><span>上一頁</span></li>`;
    }

    for(let i = 1; i <= total; i++){
        if(Number(page.currentPage) === i) {
            // str +=`<li class="page-item active"><a class="page-link" href="#" data-page="${i}">${i}</a></li>`;
            str +=`<li><a class="active" href="#" data-page="${i}">${i}</a></li>`;  // 當前頁
        } else {
            // str +=`<li class="page-item"><a class="page-link" href="#" data-page="${i}">${i}</a></li>`;
            str +=`<li><a href="#" data-page="${i}">${i}</a></li>`;
        }
    };

    if(page.hasNext) {
        // str += `<li class="page-item"><a class="page-link" href="#" data-page="${Number(page.currentPage) + 1}">下一頁</a></li>`;
        str += `<li><a href="#" data-page="${Number(page.currentPage) + 1}">下一頁</a></li>`;
    } else {
        // str += `<li class="page-item disabled"><span class="page-link">下一頁</span></li>`;
        str += `<li><span>下一頁</span></li>`;
    }

    pageid.innerHTML = str;
}
function switchPage(e){
    e.preventDefault();
    if(e.target.nodeName !== 'A') return;
    const page = e.target.dataset.page;
    pagination(jsonData,page)
}
pageid.addEventListener('click',switchPage);