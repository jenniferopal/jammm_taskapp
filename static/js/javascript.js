fetch('/all')
  .then(response => response.json())
  .then(data => {

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

// -----------------------------------------------------
// this was used to display one task on the home page hardcoded with an id, at this point we don't need it
fetch("/task_id")
  .then(response => response.json())
  .then(datta => {
      console.log("loren should be here")
      console.log(datta);
    var joke=JSON.stringify(datta);
    document.getElementById("new_task").innerHTML = joke;
  })
  .catch(err => {
      console.error('An error ocurred', err);
  });


// ----------------------------------------------------


// fetch("/task_id")
//   .then(response => response.json())
//   .then(dattta => {
//       console.log("something");
//       console.log(datta);
//       var jokke=JSON.stringify(dattta);
//       document.getElementById("loren").innerHTML = jokke;
//     })
//   .catch(err => {
//       console.error('An error ocurred', err);
//     });
    // ----------------------------------------------------
