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
    z.innerHTML = "Latitude: " + position.coords.latitude + "<br>Longitude: " + position.coords.longitude;
    x = position.coords.latitude;
    y = position.coords.longitude;
    var currentlocation = { lat: x, lng: y };
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: currentlocation
    });
    var image = 'static/carwash.png'
    var marker = new google.maps.Marker({
        position: currentlocation,
        map: map,
        tital: "my location"
    });


}

function toShowLocations() { navigator.geolocation.getCurrentPosition(showLocations); }
function showLocations(pos) {

    x = pos.coords.latitude;
    y = pos.coords.longitude;
    var currentlocation = { lat: x, lng: y };
    var image = 'static/carwash.png'
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: currentlocation
    });
    var marker = new google.maps.Marker({
        position: currentlocation,
        map: map,
        tital: "my location"
    });
    markers.forEach(function (loc) {
        var mark = new google.maps.Marker({
            position: loc.position,
            title: loc.title,
            map: map,
            icon: image,
        })
    });
    
}

function toStoreLocation() { navigator.geolocation.getCurrentPosition(storeLocation); }
function storeLocation(locat) {
    const title = document.querySelector("#title").value;
    x = document.querySelector("#lat").value;
    y = document.querySelector("#long").value;
    if ( x == "" || y == ""){
        x = locat.coords.latitude;
        y = locat.coords.longitude;
    }
    var thisLocation = {
        "lat": x,
        "long": y,
        "title": title,
    }
    console.log(thisLocation);
    const s = JSON.stringify(thisLocation);
    console.log(s);
    fetch("/saveLoc", {
        method: "POST",
        headers: {
            'Accept': 'application/json, text/plain, /',
            'Content-Type': 'application/json'
        },
        body: s,
    });
}
