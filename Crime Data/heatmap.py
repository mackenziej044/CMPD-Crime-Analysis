from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for the heat map
data = [
    {'location': [37.7749, -122.4194], 'value': 10},  # San Francisco
    {'location': [34.0522, -118.2437], 'value': 20},  # Los Angeles
    {'location': [40.7128, -74.0060], 'value': 30},   # New York
]

@app.route('/data')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
HTML File (index.html)
<!DOCTYPE html>
<html>
<head>
    <title>Heat Map</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script src="https://unpkg.com/leaflet.heat/dist/leaflet-heat.js"></script>
</head>
<body>
    <div id="map" style="height: 600px;"></div>
    <script>
        // Initialize the map
        var myMap = L.map('map').setView([37.8, -96], 4);

        // Add a tile layer
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(myMap);

        // Fetch data from the Flask API
        fetch('/data')
            .then(response => response.json())
            .then(data => {
                let heatArray = data.map(point => {
                    return [...point.location, point.value]; // [lat, lng, value]
                });

                // Create a heat layer
                L.heatLayer(heatArray, { radius: 25 }).addTo(myMap);
            });
    </script>
</body>
</html>