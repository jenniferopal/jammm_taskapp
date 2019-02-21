fetch('/all')
  .then(response => response.json())
  .then(data => {
    // var a=data


    var results=data["results"]
    // console.log("1. results", results)

    results_to_display = []
    for(var k in results) {
      var current = []
      current.push('<li id="' + results[k]['id'] + '">')
      current.push('<h2>' + results[k]['title'] + '</h2>')
        current.push('<p>' + results[k]['description'] + '</p>')
        current.push('<p class="date">' + results[k]['date'] + '</p>')
        current.push('<h4>' + results[k]['status'] + '</h4>')
        current.push('<h4>' + results[k]['urgency'] + '</h4>')
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


// fetch("/task")
//   .then(response => response.json())
//   .then(datta => {
//     // var a=data
//
//       console.log(datta);
//       // console.log(data["results"])
//     var joke=JSON.stringify(datta);
//
//     document.getElementById("muna").innerHTML = joke;
//
//   })
//   .catch(err => {
//       console.error('An error ocurred', err);
//   });
