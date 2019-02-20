// let url = "http://127.0.0.1:5002/all"
//
//  get_api_data = function httpGet(url)
//
//  {
//    var xmlHttp = new XMLHttpRequest();
//    xmlHttp.open("GET", url, false);
//    xmlHttp.send( null );
//    return xmlHttp.responseText;
//  }
//
//  let mock_json = {
//    "task_id": "1"
//  }
//
// document.getElementsById("milly").innerHTML = get_api_data()





var request = new XMLHttpRequest();

request.open('GET', 'http://127.0.0.1:5002/all', true);
request.onload = function () {

  // Begin accessing JSON data here
  var data = JSON.parse(this.response);

  if (request.status >= 200 && request.status < 400) {

      console.log(data);
    }

 else {
    console.log('error');
  }
}
}
request.send();
