---
toc: true
comments: true
layout: post
title: Parent Page for Weather application
courses: { csp: {week: 21} }
type: hacks
---
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie Check and Webpage Loader</title>
    <script>
        function checkCookiesEnabled() {
            // Try to set a test cookie
            document.cookie = "testcookie=1; path=/";

            // Try to read the test cookie
            var cookiesEnabled = document.cookie.indexOf("testcookie=") != -1;

            // Clear the test cookie
            if (cookiesEnabled) {
                document.cookie = "testcookie=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/";
            }

            return cookiesEnabled;
        }

        function loadContent() {
            if (checkCookiesEnabled()) {
                // Cookies are enabled, load the iframe
                document.getElementById("main-content").innerHTML = '<iframe src="https://drishyamody.github.io/Frontend/weather" width="100%" height="600px" style="border:none;"></iframe>';
            } else {
                // Cookies are not enabled, display error message
                document.getElementById("main-content").textContent = "403 Forbidden: Cookies are not enabled in your browser.";
            }
        }
    </script>
</head>
<body onload="loadContent()">
    <div id="main-content">
        <!-- Content will be loaded here based on cookie check -->
    </div>
</body>
</html>