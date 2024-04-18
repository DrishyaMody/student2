---
toc: True
comments: True
layout: post
title: DataStructures Writeup
courses: {'csp': {'week': 16}}
type: hacks
permalink: writeup
---

- From VSCode using SQLite3 Editor, show your unique collection/table in database, display rows and columns in the table   of the SQLite database.
<img src="http://0.0.0.0:4200/student2/images/databaseCollabora.png" height="500" width="600">  

- From VSCode model, show your unique code that was created to initialize table and create test data.

<img src="http://0.0.0.0:4200/student2/images/modelCode.png" height="500" width="600">  


Lists and Dictionaries
Blog Python API code and use of List and Dictionaries.

- In VSCode using Debugger, show a list as extracted from database as Python objects.
<img src="http://0.0.0.0:4200/student2/images/vscodevariablething.png" height="500" width="600">  

- In VSCode use Debugger and list, show two distinct example examples of dictionaries, show Keys/Values using debugger.


APIs and JSON
Blog Python API code and use of Postman to request and respond with JSON.

- In VSCode, show Python API code definition for request and response using GET, POST, UPDATE methods. Discuss algorithmic condition used to direct request to appropriate Python method based on request method.

<img src="http://0.0.0.0:4200/student2/images/getCRUD.png" height="500" width="600">  
<img src="http://0.0.0.0:4200/student2/images/postCRUD.png" height="500" width="600">  

- In VSCode, show algorithmic conditions used to validate data on a POST condition.
<img src="http://0.0.0.0:4200/student2/images/validityWriteups.png" height="400" width="1000">  

- In Postman, show URL request and Body requirements for GET, POST, and UPDATE methods.
- In Postman, show the JSON response data for 200 success conditions on GET, POST, and UPDATE methods.
<img src="http://0.0.0.0:4200/student2/images/postRequest.png" height="500" width="600">  
<img src="http://0.0.0.0:4200/student2/images/getRequest.png" height="500" width="600">  
<img src="http://0.0.0.0:4200/student2/images/putRequest.png" height="500" width="600">  

- In Postman, show the JSON response for error for 400 when missing body on a POST request.
<img src="http://0.0.0.0:4200/student2/images/400error.png" height="500" width="800">  

- In Postman, show the JSON response for error for 404 when providing an unknown user ID to a UPDATE request.

<img src="http://0.0.0.0:4200/student2/images/404error.png" height="500" width="600">  


Frontend
Blog JavaScript API fetch code and formatting code to display JSON.

- In Chrome inspect, show response of JSON objects from fetch of GET, POST, and UPDATE methods.

POST

<img src="http://0.0.0.0:4200/student2/images/inspectelement1.png" height="500" width="1000">  

GET

<img src="http://0.0.0.0:4200/student2/images/inspectelement2.png" height="500" width="1000">  

UPDATE

- In the Chrome browser, show a demo (GET) of obtaining an Array of JSON objects that are formatted into the browsers screen.
<img src="http://0.0.0.0:4200/student2/images/inspectelement3.png" height="500" width="1000">  


- In JavaScript code, describe fetch and method that obtained the Array of JSON objects.




```
function topicSearch() {
    const enteredTopic = document.getElementById("search-input").value;

    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    
    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };

    fetch("http://127.0.0.1:8086/api/post/?searchString=" + enteredTopic, requestOptions)
        .then(response => {
            if (response.ok) {
                console.log(enteredTopic + " has been searched");
                return response.json(); // Parse the JSON in the response body
            } else {
                console.error("Search failed");
                const errorMessageDiv = document.getElementById('errorMessage');
                errorMessageDiv.innerHTML = '<label style="color: red;">Search Failed</label>';
                throw new Error('Search failed');
            }
        })
        .then(data => {
            // Here 'data' is the parsed JSON object from the response body
            console.log(data); // You can see your fetched data here
            createTableFromJSON(data); // Assuming 'createTableFromJSON' expects the JSON data as parameter
        })
        .catch(error => {
            // Handle any errors that occurred during the fetch() or in the promise chain
            console.error('Error:', error);
        });
}
```

- In JavaScript code, show code that performs iteration and formatting of data into HTML.
```
              .then(data => {
            // Here 'data' is the parsed JSON object from the response body
            console.log(data); // You can see your fetched data here
             createTableFromJSON(data); // Assuming 'createTableFromJSON' expects the JSON data as parameter
         })
         .catch(error => {
             // Handle any errors that occurred during the fetch() or in the promise chain
             console.error('Error:', error);
        });
```
- In the Chrome browser, show a demo (POST or UPDATE) gathering and sending input and receiving a response that show update. Repeat this demo showing both success and failure.

FAILURE

<img src="http://0.0.0.0:4200/student2/images/postFailure.png" height="500" width="1000">  

SUCCESS

<img src="http://0.0.0.0:4200/student2/images/postSuccess.png" height="500" width="1000">  


- In JavaScript code, show and describe code that handles success. Describe how code shows success to the user in the Chrome Browser screen.
```
   fetch("http://127.0.0.1:8086/api/post/", requestOptions)
        .then(response => {
            if (response.ok) {
                console.log("Question Received");
                alert("Question has been sent, you will receive a response soon.");
              } 
              }
          )
```
- In JavaScript code, show and describe code that handles failure. Describe how the code shows failure to the user in the Chrome Browser screen.
```
else {
                console.error("Question creation failed");
                // You can handle failed login attempts here
                const errorMessageDiv = document.getElementById('errorMessage');
                errorMessageDiv.innerHTML = '<label style="color: red;">Question Creation Failed</label>';}
```
