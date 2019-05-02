// from data.js
// data = [LIST OF {OBJECTS} ]



// Assign variables
  
var tableData = data;
var button = d3.select("#click-me");
var inputValue = d3.select("#inputValue");
var dropdown = d3.select("#filterTable")

// var button = d3.select("#click-me");
// var inputValue = d3.select("#inputValue");
// var city = d3.select(".city");

//-------- Create function to report data from datetime--------//


// function init() {

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
}

// Display the entire dataset as default
// tableData.forEach(appendTable);


function getTable(filterArg) { 

// d3.event.preventDefault()
var filterArg = dropdown.property("value");
console.log("are we passing filter arg:", filterArg)
inputText = inputValue.property("value");
console.log("are we passing inputText:", inputText) 

switch (filterArg) {   
  case "dateTime":
    // Filter data set for input value based on DATETIME key
    var result = tableData.filter(obj => {
      return obj.datetime == inputText
    });
    console.log(result);
    break;

  case "city":
    var result = tableData.filter(obj => {
      return obj.city == inputText
      });
      console.log(result);
      break;

  case "state":
    var result = tableData.filter(obj => {
      return obj.state == inputText
      });
      console.log(result);
      break;

  case "country":
    var result = tableData.filter(obj => {
      return obj.state == inputText
      });
      console.log(result);
      break;

  case "shape":
    var result = tableData.filter(obj => {
      return obj.state == inputText
      });
      console.log(result);
      break;
    
  default:
      var result = tableData.filter(obj => {
        return obj.datetime == inputText
      });
      console.log(result);
      break;
    
    console.log("none")
    break;
  }  

  // console.log("are we passing filter result:", result)

    // First clear all table data from previous query
    d3.selectAll("td").remove();

    // Pull input value 
   

    // Clear input value
    inputValue.property("value", "");

    return result.forEach(appendTable);
  }

  //  result.forEach(appendTable);

// Add event listener for submit button
d3.select("#click-me").on("click", getTable);

