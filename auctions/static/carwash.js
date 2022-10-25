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

    fetch("/loc")
        .then(response => response.json())
        .then(locations => {
            locations.forEach(function (loc) {
                var tit = loc.name;
                var mark = new google.maps.Marker({
                    position: { lat: loc.lat, lng: loc.long },
                    title: tit,
                    map: map,
                    icon: image,
                })
            });
        })

}

function toStoreLocation() { navigator.geolocation.getCurrentPosition(storeLocation); }
function storeLocation(locat) {
    x = locat.coords.latitude;
    y = locat.coords.longitude;
    const title = document.querySelector("#title").value;
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
