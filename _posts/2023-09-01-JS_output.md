---
layout: post
title: Personalized JS output w/ jquery
type: hacks
description: My favorite soccer players!
courses: {"csp": {"week": 2}}
permalink: /JSoutput-w/Jquery
---




<!-- Head contains information to Support the Document -->
<head>
    <!-- load jQuery and DataTables output style and scripts -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
    <script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>var define = null;</script>
    <script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
</head>

<!-- Body contains the contents of the Document -->
<body>
    <table id="demo" class="table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Club</th>
                <th>BirthYear</th>
                <th>Country</th>
                <th>NetWorth</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Lionel Messi</td>
                <td>Inter Miami</td>
                <td>1987</td>
                <td>Argentina</td>
                <td>$600 Million</td>
            </tr>
            <tr>
                <td>Cristiano Ronaldo</td>
                <td>Al Nassar</td>
                <td>1985</td>
                <td>Portugal</td>
                <td>$500 Million</td>
            </tr>
            <tr>
                <td>Neymar Jr.</td>
                <td>Al Hilal</td>
                <td>1992</td>
                <td>Brazil</td>
                <td>$250 Million</td>
            </tr>
            <tr>
                <td>Kylian Mbappe</td>
                <td>PSG</td>
                <td>1998</td>
                <td>France</td>
                <td>$180 Million</td>
            </tr>
            <tr>
                <td>Bukayo Saka</td>
                <td>Arsenal</td>
                <td>2001</td>
                <td>English</td>
                <td>$2 Million</td>
            </tr>
            <tr>
                <td>Phil Fodena</td>
                <td>Manchester City</td>
                <td>2000</td>
                <td>English</td>
                <td>$12 Million</td>
            </tr>
            <tr>
                <td>Robert Lewandowski</td>
                <td>Barcelona</td>
                <td>1988</td>
                <td>Poland</td>
                <td>$90 Million</td>
            </tr>
            <tr>
                <td>Trent Alexander-Arnold</td>
                <td>Liverpool</td>
                <td>1998</td>
                <td>England</td>
                <td>$3 Million</td>
            </tr>
            <tr>
                <td>Erling Haaland</td>
                <td>Manchester City</td>
                <td>2000</td>
                <td>Norway</td>
                <td>$9 Million</td>
            </tr>
            <tr>
                <td>Kevin De Bruyne</td>
                <td>Manchester City</td>
                <td>1991</td>
                <td>Belgium</td>
                <td>$45 Million</td>
            </tr>
        </tbody>
    </table>
</body>

<!-- Script is used to embed executable code -->
<script>
    $("#demo").DataTable();
</script>