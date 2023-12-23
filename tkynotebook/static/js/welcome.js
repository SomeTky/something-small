function myFunction() {  
  var account = document.getElementById('user_account').value;
  var password = document.getElementById('password').value;
  
  if (!account) {
    document.getElementById('login_res').innerHTML = "账号不能为空";
    return ;
  }
  if (!password) {
    document.getElementById('login_res').innerHTML = "密码不能为空";
    return ;
  }

  var url = "/login";
  var httpRequest = new XMLHttpRequest();
  httpRequest.open('POST', url, true);
  httpRequest.setRequestHeader("Content-type", "application/json");
  httpRequest.send(JSON.stringify({'account': account, 'password': password}));

  // 响应后的回调函数
  httpRequest.onreadystatechange = function () {
    if (httpRequest.readyState == 4 && httpRequest.status == 200) {
        var access = httpRequest.responseText;
        if (access == "账号不存在" || access == "密码错误") {
          document.getElementById('login_res').innerHTML = access;
          return;
        }
        localStorage.setItem('access', access);
        next_page = "/homepage?access=" + access;
        location.replace(next_page);
    }
  };
}


window.onload = function check_access() {
  var access = localStorage.getItem('access');
  if (!access) return;
  next_page = "/homepage?access=" + access;
  location.replace(next_page);
}