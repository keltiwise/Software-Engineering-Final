# Software Engineering Final
## Templates
HTML files stored in this branch to organize and display content. Each file in this branch corresponds to a different page on the website that can be accessed. 

## About HTML
HTML file organizes content that is shown on the about page of the website.

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="{{ url_for('static', filename= 'css/navigation-example.css') }}">
    <title>About</title>
</head>
<body>
    <div class="header">
        <h1>CS 188 Brewery Project</h1>
    </div>
    <div class="topnav"> 

        {% for item in nav.top %}
        <a class="{{ 'active' if item.is_active else '' }}" href="{{ item.url }}">{{ item.label }}</a>
        {% endfor %} 
    </div>
    <br>
   <p>Talk about project here and how to use...
   </p>
</body>
</html>
```

## Chat HTML
HTML file that organizes how users can interact with one another through a chat feature on the website. 

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="{{ url_for('static', filename= 'css/navigation-example.css') }}">
    <title>Chat</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.4/css/jquery.dataTables.css">
</head>
<body>
    <div class="header">
        <h1>CS 188 Brewery Project</h1>
    </div>
    <div class="topnav"> 
        {% for item in nav.top %}
        <a class="{{ 'active' if item.is_active else '' }}" href="{{ item.url }}">{{ item.label }}</a>
        {% endfor %} 
    </div>
    <br>
    <textarea id="userInput" name="userInput" rows="10" cols="50"></textarea>
    <br>
    <button class="buttonAdd" onclick="addEntry()">Post Chat</button>
    <div class="buttonContainer2">
        <input id="chatIDdelete" class="inputDelete" placeholder="Enter Chat ID to Delete"> 
        <input id="passwordDelete" type="password" class="inputAdd" placeholder="Enter Password">
        <button class="buttonDelete" onclick="deleteEntry()">Delete</button>
    </div>
    <table id="chatTable" class="display">
        <thead>
            <tr>
                <th>ChatID</th>
                <th>Chat</th>
            </tr>
        </thead>
        <tbody>
            {% for record in records %}
            <tr>
                <td>{{ record[0] }}</td>
                <td>{{ record[1] }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    <script>
        $(document).ready(function() {
            $('#chatTable').DataTable();
        });

        function addEntry() {
            var userInput = document.getElementById('userInput').value;

            fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: 'action=add&Chat=' + encodeURIComponent(userInput),
            })
            .then(response => {
                if (response.ok) {
                    return response.text();
                } else {
                    console.error('Error adding entry');
                }
            })
            .then(data => {
                if (data === "Entry added successfully") {
                    window.location.reload();
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }

    function deleteEntry() {
        var chat_ID = document.getElementById('chatIDdelete').value; 
        var password = document.getElementById('passwordDelete').value;

        if (password !== 'edit') { 
            console.error('Incorrect password');
            return; 
        }

        fetch('/chat', {  
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'action=delete&ChatID=' + encodeURIComponent(chat_ID),
        })
        .then(response => {
            if (response.ok) {
                return response.text();
            } else {
                console.error('Error deleting entry');
            }
        })
        .then(data => {
            if (data === "Entry deleted successfully") {
                window.location.reload();
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
    </script>
</body>
</html>
```

## Database HTML
HTML file that organizes how the database is displayed and stored on our website in which users can interact with it.

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="{{ url_for('static', filename= 'css/navigation-example.css') }}">
    <link rel="stylesheet" href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.css">
    <title>Database</title>
</head>
<body>
    <div class="header">
        <h1>CS 188 Brewery Project </h1>
    </div>
    <div class="topnav"> 
        {% for item in nav.top %}
        <a class="{{ 'active' if item.is_active else '' }}" href="{{ item.url }}">{{ item.label }}</a>
        {% endfor %} 
    </div>
    <br>
    <table id="barTable" class="display">
        <thead>
            <tr>
                <th>BarID</th>
                <th>Latitude</th>
                <th>Longitude</th>
                <th>Name</th>
                <th>Positive Ratings</th>
                <th>Negative Ratings</th>
            </tr>
        </thead>
        <tbody>
            {% for record in records %}
            <tr>
                <td>{{ record[0] }}</td>
                <td>{{ record[1] }}</td>
                <td>{{ record[2] }}</td>
                <td>{{ record[3] }}</td>
                <td>{{ record[4] }}</td>
                <td>{{ record[5] }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    <div class="buttonContainer">
        <input id="updateID" class="inputUpdate" placeholder="Enter Bar ID"> 
        <input id="updateLatitude" class="inputUpdate" placeholder="Enter New Latitude">
        <input id="updateLongitude" class="inputUpdate" placeholder="Enter New Longitude">
        <input id="updateName" class="inputUpdate" placeholder="Enter New Bar Name">
        <input id="updatePositive" class="inputUpdate" placeholder="Enter Positive Ratings">
        <input id="updateNegative" class="inputUpdate" placeholder="Enter Negative Ratings">
        <input id="passwordUpdate" type="password" class="inputUpdate" placeholder="Enter Password"> 
        <button class="buttonUpdate" onclick="updateEntry()">Update</button>
    </div>

    <div class="buttonContainer">
        <input id="addLatitude" class="inputAdd" placeholder="Enter Latitude">
        <input id="addLongitude" class="inputAdd" placeholder="Enter Longitude">
        <input id="addName" class="inputAdd" placeholder="Enter Bar Name">
        <input id="passwordAdd" type="password" class="inputAdd" placeholder="Enter Password"> 
        <button class="buttonAdd" onclick="addEntry()">Add</button>
    </div>
    
    <div class="buttonContainer">
        <input id="barIDdelete" class="inputDelete" placeholder="Enter Bar ID"> 
        <input id="passwordDelete" type="password" class="inputAdd" placeholder="Enter Password">
        <button class="buttonDelete" onclick="deleteEntry()">Delete</button>
    </div>

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.js"></script>
    <script>
        $(document).ready(function() {
            $('#barTable').DataTable();
        });


    function addEntry() {
    var latitude = document.getElementById('addLatitude').value;
    var longitude = document.getElementById('addLongitude').value;
    var BarName = document.getElementById('addName').value;
    var password = document.getElementById('passwordAdd').value; 
    var BarName = document.getElementById('addName').value;
    var password = document.getElementById('passwordAdd').value; 

    if (password !== 'edit') { 
        console.error('Incorrect password');
        return; 
    }

    fetch('/database', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'action=add&Latitude=' + encodeURIComponent(latitude) + '&Longitude=' + encodeURIComponent(longitude) + '&BarName=' + encodeURIComponent(BarName),
    })
    .then(response => {
        if (response.ok) {
            window.location.reload();
        } else {
            console.error('Error adding entry');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
    }


    function updateEntry() {
    var barID = document.getElementById('updateID').value; 
    var latitude = document.getElementById('updateLatitude').value;
    var longitude = document.getElementById('updateLongitude').value;
    var barname = document.getElementById('updateName').value;
    var password = document.getElementById('passwordUpdate').value; 
    var positive = document.getElementById('updatePositive').value;
    var negative = document.getElementById('updateNegative').value; 

    if (password !== 'edit') { 
        console.error('Incorrect password');
        return; 
    }

    fetch('/database', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'action=update&BarID=' + encodeURIComponent(barID) + '&Latitude=' + encodeURIComponent(latitude) + '&Longitude=' + encodeURIComponent(longitude) + 
        '&BarName=' + encodeURIComponent(barname) + '&PositveRatings=' + encodeURIComponent(positive) + '&NegativeRatings=' + encodeURIComponent(negative),
    })
    .then(response => {
        if (response.ok) {
            window.location.reload();
        } else {
            console.error('Error updating entry');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
    }
    
    function deleteEntry() {
    var BarID = document.getElementById('barIDdelete').value; 
    var password = document.getElementById('passwordDelete').value;

    if (password !== 'edit') { 
        console.error('Incorrect password');
        return; 
    }

    fetch('/database', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'action=delete&BarID=' + encodeURIComponent(BarID),
    })
    .then(response => {
        if (response.ok) {
            // Reload the page to reflect changes
            window.location.reload();
        } else {
            // Handle error
            console.error('Error deleting entry');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
    }
    </script>
</body>
</html>

```

## Home HTML
HTML that organizes and stuctures the home page on the website.

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="{{ url_for('static', filename= 'css/navigation-example.css') }}">
    <title>Home</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
</head>
<body>
    <div class="header">
        <h1>CS 188 Brewery Project</h1>
    </div>
    <div class="topnav"> 
        {% for item in nav.top %}
        <a class="{{ 'active' if item.is_active else '' }}" href="{{ item.url }}">{{ item.label }}</a>
        {% endfor %} 
    </div>
    <div id="map">
    </div>
</body>
<script>
    var map = L.map('map').setView([41.6031, -93.6546], 16); 

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    {% for record in records %}
    var redMarker = L.marker([{{ record.Latitude }}, {{ record.Longitude }}], {
        icon: L.divIcon({
            className: 'custom-div-icon',
            html: "<div class='marker-dot' style='background-color: Maroon; border: 2px solid black; width: 10px; height: 10px; border-radius: 50%;'></div>",
            iconSize: [20, 20],
            iconAnchor: [10, 10]
        })
    }).addTo(map);

    redMarker.bindTooltip("Bar Name: {{ record.BarName }}, Positive Ratings: {{ record.PositiveRatings }}, Negative Ratings: {{ record.NegativeRatings }}");
    {% endfor %}
</script>
</html>
```

## Review HTML
HTML to structure the review page, where users can leave reviews of the brewery they visited.

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="{{ url_for('static', filename= 'css/navigation-example.css') }}">
    <title>Review</title>
</head>
<body>
    <div class="header">
        <h1>CS 188 Brewery Project</h1>
    </div>
    <div class="topnav"> 
        {% for item in nav.top %}
        <a class="{{ 'active' if item.is_active else '' }}" href="{{ item.url }}">{{ item.label }}</a>
        {% endfor %} 
    </div>
    <br>
    <form action="#" method="post">
        <select name="barID" style = "width: 300px;">
            {% for bar in bars %}
            <option value="{{ bar.BarID }}">{{ bar.BarName }}</option>
            {% endfor %}
        </select>
        <br><br>
        <textarea name="userInput" rows="10" cols="50"></textarea>
        <br>
        <button class="buttonAdd" onclick="addEntry()">Submit Review</button>
    </form>
</body>
</html>
```
