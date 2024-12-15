// Create map
var map = L.map('map').setView([0, 0], 4); // Adjusted to valid coordinates

// Add tile layer
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// Initialize all the LayerGroups that we'll use.
let layers = {
    HEAT_MAP: new L.LayerGroup(),
};

// Add the layer groups to the map initially
layers.HEAT_MAP.addTo(map);

// Create an overlays object to add to the layer control.
let overlays = {
    "Crimes Reported": layers.HEAT_MAP,
};

// Create a control for our layers, and add our overlays to it.
L.control.layers(null, overlays).addTo(map);

// Create a legend to display information about our map.
let info = L.control({
    position: "bottomright"
});

// When the layer control is added, insert a div with the class of "legend".
info.onAdd = function() {
    let div = L.DomUtil.create("div", "legend");
    div.innerHTML = '<h4>Legend</h4><i style="background: #ff7800"></i> Crimes Reported<br><i style="background: #0080ff"></i> UFO Sightings';
    return div;
};

// Add the info legend to the map.
info.addTo(map);

// Fetch data from the Flask API
fetch('/data')
.then(response => response.json())
.then(data => {
    let heatArray = data.map(point => {
        return [point.location[0], point.location[1], point.value]; // [lat, lng, value]
    });

    // Create a heat layer
    L.heatLayer(heatArray, { radius: 25 }).addTo(map); // Changed myMap to map
});