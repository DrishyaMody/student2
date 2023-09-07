---
layout: post
title: JS Input
type: hacks
courses: {"csp": {"week": 3}}
permalink: /JSinput
---
<!-- Heading -->
<h1>GPA Calculator</h1>
<h2>AP Input Grades</h2>
<!-- Totals -->
<h3>
    Total : <span id="total">0.0</span>
    Number of Classes : <span id="count">0.0</span>
    GPA : <span id="average">0.0</span>
</h3>
<!-- Rows -->
<div id="scores">
    <!-- javascript generated inputs -->
</div>

<script>
// Creates a new input box
function newInputLine(index) {


    // Add a label for each score element
    var title = document.createElement('label');
    title.htmlFor = index;
    title.innerHTML = (index + 1) + ". ";    
    document.getElementById("scores").appendChild(title); // add to HTML


    var option_text = ["---","A","B","C","D","F"]
    var option_value = ["",5,4,3,2,1]
    var score = document.createElement("select"); //dropdownmenu
    score.id = index; // id of select control
    score.onkeydown = calculator //call calculator function(when tab or enter is hit uses the data for calculations)
    score.name = "score";  // name is used to group "score" elements
    document.getElementById("scores").appendChild(score); 
    // Create and add blank line after input box
    var br = document.createElement("br");  // line break element
    document.getElementById("scores").appendChild(br); // add to HTML
    //Create and append the options
    for (var i = 0; i < option_text.length; i++) {
        var option = document.createElement("option");
        option.value = option_value[i];
        option.text = option_text[i];
        score.appendChild(option);
    }

    // Set focus on the new input line
    document.getElementById(index).focus();
}

// Handles event and calculates totals
function calculator(event) {
    var key = event.key;
    // Check if the pressed key is the "Tab" key (key code 9) or "Enter" key (key code 13)
    if (key === "Tab" || key === "Enter") { 
        event.preventDefault(); // Prevent default behavior (tabbing to the next element)
   
        var array = document.getElementsByName('score'); // setup array of scores
        var total = 0;  // running total
        var count = 0;  // count of input elements with valid values

        for (var i = 0; i < array.length; i++) {  // iterate through array
            var value = array[i].value;
            if (parseFloat(value)) {
                array[i].style.backgroundColor = "lightGrey"
                var parsedValue = parseFloat(value);
                total += parsedValue;  // add to running total
                count++;
            }
        }


        // update totals
        document.getElementById('total').innerHTML = total.toFixed(2); // show two decimals
        document.getElementById('count').innerHTML = count ;

        if (count > 0) {
            document.getElementById('average').innerHTML = (total / count).toFixed(2);
        } else {
            document.getElementById('average').innerHTML = "0.0";
        }

        // adds newInputLine, only if all array values satisfy parseFloat 
        if (count === document.getElementsByName('score').length) {
            newInputLine(count); // make a new input line
        }
    }
}

// Creates 1st input box on Window load
newInputLine(0);

</script>