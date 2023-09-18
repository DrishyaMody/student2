---
toc: true
comments: true
layout: post
title: JS itunes w/ API
courses: {"csp": {"week": 5} }
type: hacks
---

<html lang="en">
<head>
    <title>Song Search</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
        }
        #container {
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin: 20px auto;
            max-width: 600px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        #search-box {
            text-align: center;
            margin-bottom: 20px;
        }
        #song-search {
            padding: 10px;
            width: 80%;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        #search-button {
            padding: 10px 20px;
            background-color: #ff5722;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        #search-button:hover {
            background-color: #f44336;
        }
        #results {
            text-align: center;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 20px 0;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        img {
            max-width: 150px;
            max-height: 150px;
        }
    </style>
</head>
<body>
    <div id="container">
        <h1>Song Search</h1>
        
        <div id="search-box">
            <label for="song-search">Search for a song:</label>
            <input type="text" id="song-search" placeholder="Enter a song title">
            <button id="search-button">Search</button>
        </div>
        
        <div id="results">
            <h2>Search Results</h2>
            <ul id="song-list"></ul>
        </div>
    </div>

    <script>
        document.getElementById("search-button").addEventListener("click", function () {
            const searchTerm = document.getElementById("song-search").value;
            searchForSongs(searchTerm);
        });

        function searchForSongs(searchTerm) {
            // Use the iTunes Search API to fetch song data
            const apiUrl = `https://itunes.apple.com/search?term=${searchTerm}&entity=song&limit=10`;

            fetch(apiUrl)
                .then(response => response.json())
                .then(data => {
                    displayResults(data.results);
                })
                .catch(error => {
                    console.error("Error fetching data: ", error);
                });
        }

        function displayResults(results) {
            const songList = document.getElementById("song-list");
            songList.innerHTML = "";

            if (results.length === 0) {
                songList.innerHTML = "<p>No songs found</p>";
                return;
            }

            results.forEach(song => {
                const listItem = document.createElement("li");
                const albumImage = document.createElement("img");
                albumImage.src = song.artworkUrl100;
                listItem.appendChild(albumImage);
                listItem.innerHTML += `<strong>${song.trackName}</strong> by ${song.artistName}`;
                // Add an audio sample
                listItem.innerHTML += `<audio controls><source src="${song.previewUrl}" type="audio/mpeg"></audio>`;
                songList.appendChild(listItem);
            });
        }
    </script>
</body>
</html>