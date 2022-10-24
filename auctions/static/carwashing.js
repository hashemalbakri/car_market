var z = document.getElementById("demo");
var x;
var y;

var map;
var markers = [
    {
        position: { lat: 33.398165, lng: 44.3960218 },
        title: 'first'
    },
    {
        position: { lat: 33.3676544, lng: 44.3580416 },
        title: 'second'
    },
    {
        position: { lat: 33.3364, lng: 44.4004 },
        title: 'third'
    }
];

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
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: currentlocation
    });
    var image = 'static/carwash.png'
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
    x = locat.coords.latitude;
    y = locat.coords.longitude;
    const title = document.querySelector("#title").value;
    var thisLocation = {
        'lat': x,
        'long': y,
        // title: title,
    }
    console.log(thisLocation);
    const s = JSON.stringify(thisLocation);
    console.log(s);
    fetch("/test", {
        method: "POST",
        headers: {
            'Accept': 'application/json, text/plain, /',
            'Content-Type': 'application/json'
        },
        body: s,
    });
}
