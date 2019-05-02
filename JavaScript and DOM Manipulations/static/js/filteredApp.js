// Assign variables
  
var tableData = data;
var button = d3.select("#click-me");
var inputValue = d3.select("#inputValue");
var dropdown = d3.select("#filterTable")

//-------- Create function to report data from datetime--------//


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

// Create function to pass in dropdown values, filter table data, and return appended table
function getTable(filterArg) { 

// Create variable to be passed into switch statement, based on input
var filterArg = dropdown.property("value");
console.log("We are passing filter arg:", filterArg)
inputText = inputValue.property("value");
console.log("We are passing inputText:", inputText) 

// Prevent the page from refreshing
d3.event.preventDefault();

// Create switch statement to filter data set based on dropdown value
switch (filterArg) {   
  case "dateTime":
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
      console.log("None Found");
      break;
  }  

    // Clear all table data from previous query
    d3.selectAll("td").remove();

    // Clear input value from previous query
    inputValue.property("value", "");

    // Return results from filter argument & use function to append table
    return result.forEach(appendTable);
  }


// Add event listener for submit button
d3.select("#click-me").on("click", getTable);