fetch('/all')
  .then(response => response.json())
  .then(data => {
    // var a=data

      // console.log(data);
      // console.log(data["results"])
    var hello=JSON.stringify(data);
    var mari=data["results"]
    var muna=JSON.stringify(mari);
    var milly=mari[0]
    // console.log(milly);
    var jen=JSON.stringify(milly);
    // var beta=data.results;
    // var muna= hello[198]

    document.getElementById("milly").innerHTML = muna;
    // document.getElementById("milly").innerHTML = hello;


  })
  .catch(err => {
      console.error('An error ocurred', err);
  });


fetch("/task")
  .then(response => response.json())
  .then(datta => {
    // var a=data

      console.log(datta);
      // console.log(data["results"])
    var joke=JSON.stringify(datta);
    // var mari=data["results"]
    // var muna=JSON.stringify(mari);
    // var milly=mari[0]
    // console.log(milly);
    // var jen=JSON.stringify(milly);
    // var beta=data.results;
    // var muna= hello[198]

    document.getElementById("muna").innerHTML = joke;
    // document.getElementById("milly").innerHTML = hello;


  })
  .catch(err => {
      console.error('An error ocurred', err);
  });




  fetch("/task")
    .then(response => response.json())
    .then(dattta => {
        console.log(datta);
      var jokke=JSON.stringify(dattta);
      document.getElementById("new_task").innerHTML = jokke;
    })
    .catch(err => {
        console.error('An error ocurred', err);
    });
