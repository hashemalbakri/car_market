var z = document.getElementById("demo");
var x;
var y;

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        z.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    z.innerHTML = "Latitude: " + position.coords.latitude +
        "<br>Longitude: " + position.coords.longitude;

    x = position.coords.latitude;
    y = position.coords.longitude;

    var currentlocation = { lat: x, lng: y };
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 14,
        center: currentlocation
    });
    var marker = new google.maps.Marker({
        position: currentlocation,
        map: map
    });
}
