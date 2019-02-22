fetch('/all')
  .then(response => response.json())
  .then(data => {
    // var a=data


    var results=data["results"]
    // console.log("1. results", results)

    results_to_display = []
    for(var k in results) {
      var current = []
      current.push('<li class="col-md-3" id="' + results[k]['id'] + '">')
      current.push('<h3>' + results[k]['title'] + '</h3>')
        current.push('<p> <strong>Description: </strong>' + results[k]['description'] + '</p>')
        current.push('<p>  <strong>Date: </strong>' + results[k]['date'] + '</p>')
        current.push('<h6> <strong>Status: </strong>' + results[k]['status'] + '</h6>')
        current.push('<h6> <strong>Urgency: </strong>' + results[k]['urgency'] + '</h6>')
        current.push('<button type="button" class="btn btn-secondary btn-sm">Edit</button>')
        current.push('<a href="/task_delete/'+ results[k]['title'] + '" class="btn btn-secondary btn-sm">Delete</a>')
        current.push('</li>')
      results_to_display.push(current.join(""))

      console.log("2. ", results[k])
      // console.log("3. ", current)

    }
    document.getElementById("results").innerHTML = results_to_display.join("");


  })
  .catch(err => {
      console.error('An error ocurred', err);
  });
