// from data.js

// data = [LIST OF {OBJECTS} ]

// var data = [{
//     datetime: "1/1/2010",
//     city: "benton",
//     state: "ar",
//     country: "us",
//     shape: "circle",
//     durationMinutes: "5 mins.",
//     comments: "4 bright green circles high in the sky going in circles then one bright green light at my front door."
//   },

  
var tableData = data;
// var inputField = d3.select("#input-field");
var button = d3.select("#click-me");
var date = d3.select("#date");

var city = d3.select(".city");


//-------- Create function to report data from datetime--------//

  // Input Date
  date.on("change", function handleChange() { 
    var inputText = d3.event.target.value;
    console.log("You entered: " + inputText);

    // Filter data set for input value based on DATETIME key
    var result = tableData.filter(obj => {
      return obj.datetime === inputText
    });

    console.log(result)
    
    // Define a function to append table based on reports data
    function appendTable(report) {
      var tbody = d3.select("tbody");

      // add a new row
      var row = tbody.append("tr");

      // for each key value pair in an object
      Object.entries(report).forEach(([key, value]) => {

          // add a new cell
          var cell = row.append("td");
          cell.text(value);

          // set a class for comments to align text differently
          if (key === "comments") {
              cell.attr("class", "record-comments")
          }
        });
      };

      // Call function with output of search
      return result.forEach(appendTable);
  });









    // result.forEach(function(d) { 
    // var resultCity = d.city;
    // var resultState = d.state;
    // var resultCountry = d.country;
    // var resultShape = d.shape;
    // var resultDuration = d.durationMinutes;
    // var resultComments = d.comments;

    // city.text(resultCity);

    // result.forEach(function tabulate(data, columns) {

    // d3.json('data.js', function (error,data) {

    //   function tabulate(data, columns) {
    //     var table = d3.select('body').append('table')
    //     var thead = table.append('thead')
    //     var	tbody = table.append('tbody');
      
    //     // append the header row
    //     thead.append('tr')
    //       .selectAll('th')
    //       .data(columns).enter()
    //       .append('th')
    //         .text(function (column) { return column; });
      
    //     // create a row for each object in the data
    //     var rows = tbody.selectAll('tr')
    //       .data(data)
    //       .enter()
    //       .append('tr');
      
    //     // create a cell in each row for each column
    //     var cells = rows.selectAll('td')
    //       .data(function (row) {
    //         return columns.map(function (column) {
    //           return {column: column, value: row[column]};
    //         });
    //       })
    //       .enter()
    //       .append('td')
    //         .text(function (d) { return d.value; });
      
    //     return table;
    //   }
      
   
    // // render the table(s)
    // tabulate(data, ['City', 'Comments','Country', 'DateTime', 'Duration','Shape', 'State']); // 7 column table



    
  // <td class="table-head city">City</td>
  // <th class="table-head">State</th>
  // <th class="table-head">Country</th>
  // <th class="table-head">Shape</th>
  // <th class="table-head">Duration</th>
  // <th class="table-head">Comments</th>
    



// function handleChange(event) {
//   // grab the value of the input field
//   var inputText = d3.event.target.value;

//   // reverse the input string
//   // var reversedInput = reverseString(inputText);

//   // Set the output text to the reversed input string
//   // output.text(reversedInput);
//   console.log(inputText);
// }

// date.on("change", handleChange);



// // This code could turn each Value from a given Key into a variable
// // var datetime = data.map(d => d.datetime)
// //   console.log(datetime)

// // Exploring data
// console.log(tableData) // {datetime: "1/1/2010", city: "benton", state: "ar", country: "us", shape: "circle", …}
// console.log(tableData[0].datetime) // "1/10/2010"


// // This code works to search the datetime field and result a list of all objects from that date
// var result = data.filter(obj => {
//   return obj.datetime === "1/1/2010"
// })

// // Exploring data
// console.log(result[0].datetime) // 1/1/2010
// console.log(result[0].state) // ar

// result.forEach(function(d) { 
//   console.log(d.state)
// }); // Returns print of each dictionary AND whatever value for the key that is defined


// inputField.on("change", function() {
//   var newText = d3.event.target.value;
//   console.log(newText);


// function to handle input change
// function handleChange(event) {
//   // grab the value of the input field
//   var inputText = d3.event.target.value;

//   console.log(inputText);

// }

// text.on("change", handleChange);



// button.on("click", function() { 
  // var newText = d3.event.target.value;
  // var result = data.filter(obj => {
  //   console.log(obj.datetime === newText)
  //   console.log(result)};


// var result = data.filter(obj => {
//   console.log(obj.datetime === newText)
// });

  // result.forEach(function(d) { 
  //   var resultCity = d.city;
  //   var resultState = d.state;
  //   var resultCountry = d.country;
  //   var resultShape = d.shape;
  //   var resultDuration = d.durationMinutes;
  //   var resultComments = d.comments;
  //   console.log(resultCity, resultState, resultCountry, resultShape, resultDuration, resultComments);
  //   });


// //date/time, city, state, country, shape, and comment
// <th class="table-head">City</th>
// <th class="table-head">State</th>
// <th class="table-head">Country</th>
// <th class="table-head">Shape</th>
// <th class="table-head">Duration</th>
// <th class="table-head">Comments</th>
