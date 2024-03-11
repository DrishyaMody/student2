---
comments: True
layout: post
title: Individual final 
courses: {'csp': {'week': 23}}
type: hacks
---

<img src="https://drishyamody.github.io/student2/images/partCcbreq.png"  height="400" width="700">  

### MY INDIVIDUAL FEATURES ###

<img src="https://drishyamody.github.io/student2/images/backendfeature.png" alt="Backend for Feature 1" height="400" width="400"> 
 <img src="https://drishyamody.github.io/student2/images/frontendgeature.png" alt="Frontend for Feature 1" height="400" width="400"> 
 <img src="https://drishyamody.github.io/student2/images/featuretwobackend.png" alt="Backend for Feature 2" height="400" width="400"> 
 <img src="https://drishyamody.github.io/student2/images/featuretwofrontend.png" alt="Frontend for Feature 2" height="400" width="400"> 


- Added the backend POST method and function to allow users to ask a question publicly, after testing the functionality through postman, I fetched this on the frontend as shown. 


### Requirement 1: ###    
        Instructions for input for one of the following
            - the user(including user actions that trigger events)
            - a device
            - an online data stream
            - a file

- How I adressed the first CPT requirement 

   FEATURE 1: I required user to input a question that they are curious about. I required the question to have a minimum of 10 characters. Once the user posts a question it is then stored in our sqlite database and alerts the user that their question has been saved and that they will recieve a response soon. 

   FEATURE 2: After the user searches for a question from the database they are redirected to a dynamic webpage in which it will display whichever question they have chosen to either respond to or view responses too. In the function defined as reply_api in the frontend it requires input from the user so that the comment can be posted. Once the user hits enter the browser will alert them saying that their response has been received then the page automatically refreshes and portrays their response in a formatted fashion. This response will now be visible to anyone that views the question. The formatted response also displays the username of the user that posted it. 

### Requirement 2: ###
Use at least one list (or other collection type) to represent collection of data that is stored to manage program complexity and help fulfill the programs purpose.

- How I adressed the second CPT requirement

    <img src="https://drishyamody.github.io/student2/images/reqtwopicone.png" height="400" width="700">
    <img src="https://drishyamody.github.io/student2/images/reqtwopictwo.png" height="400" width="700">
    <img src="https://drishyamody.github.io/student2/images/rectwopicthree.png" height="400" width="700">
       

    FEATURE 1: After the user inputs their question and the browser alerts them that their question has been sent and that they will recieve a response soon, their question gets stored onto our sqlite database with a unique id as shown in the image of our POSTS datbase. 

    FEATURE 2: After the user inputs their response/comment on a specfic question their response is also stored on our sqlite database and has its own unique id and is also appended as a child under the unique id of the question as demonstrated by the image above. 


### Requirement 3: ###
Included parameters in my programs are, the userid or to the user displayed as the username, the date of the question asked which is stored in the database as "doq", the parentPostId which is the id of a question stored inside of the id of the user. So if we were to test a GET method of a specific user it would also show under their id their quesitons and responses. The note parameter in the POSTS database stores the questions. 


### KEY COMMITS ###
[Commit1](https://github.com/DrishyaMody/CollaboraDJAK/commit/66891110ecebf87dc1cc7e9b7d1d676eddd5cc9e)

[Commit2](https://github.com/DrishyaMody/CollaboraDJAK/commit/963064e6d3fb69f41b933eb77592b81ce7e0b7da#diff-8b59579ab8d325a01df5affb5a3a867271d8e46391eb0fb36231a8cb083ed9fb)

<img src="https://drishyamody.github.io/student2/images/commitContributions.png" height="400" width="700">





My Trimester 2 grade: 
<img src="https://drishyamody.github.io/student2/images/cspgrade.png" height="400" width="700">


### OVERALL RETROSPECTIVE ###

Throughout this process I realised my potential for leadership and problem solving. Throughout the process of making Collabora I was exposed to the true power of agile methodology and working efficentely together as a team. This enlightened not only my capabilities as a leader but also my strenghts at problem solving and my desire to acheive the end result despite the external factors like time and lathargy that come into play.