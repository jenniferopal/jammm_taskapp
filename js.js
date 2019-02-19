
  let url = "http://127.0.0.1:8080/taskapi/6"

  get_api_data = function httpGet(url)

  {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", url, false);
    xmlHttp.send( null );
    return xmlHttp.responseText;
  }

  let mock_json = {
    "task_id": "1"
  }

  document.getElementsById("milly").innerHTML = get_api_data()
