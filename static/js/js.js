fetch('/all')
  .then(response => response.json())
  .then(data => {
    // var a=data


    var results=data["results"]
    // console.log("1. results", results)

    results_to_display = []
    for(var k in results) {
      var current = []
      current.push('<li class="col-md-3 mt-4" id="' + results[k]['id'] + '">')
      current.push('<p><strong>' + results[k]['title'] + '</strong></p>')
        current.push('<p>' + results[k]['description'] + '</p>')
        current.push('<p class="date">' + results[k]['date'] + '</p>')
        current.push('<h6>' + results[k]['status'] + '</h6>')
        current.push('<h6>' + results[k]['urgency'] + '</h6>')
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
