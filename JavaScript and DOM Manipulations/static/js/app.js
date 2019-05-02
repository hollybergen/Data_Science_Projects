// Assign variables
  
var tableData = data;
var button = d3.select("#click-me");
var date = d3.select("#date");
var city = d3.select(".city");

//-------- Create function to report data from datetime--------//


  // Input Date
  button.on("click", function handleChange() { 

    // First clear all table data from previous query
    d3.selectAll("td").remove();

    // Pull input value 
    inputText = date.property("value");

    // Filter data set for input value based on DATETIME key
    var result = tableData.filter(obj => {
      return obj.datetime === inputText
    });
   
    // Clear input value
    date.property("value", "");

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