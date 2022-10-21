var z = document.getElementById("demo");
var x;
var y;
var map;
var markers = [
    {
        position: {lat: 33.398165, lng: 44.3960218},
        title:'first'
    },
    {
        position: {lat: 33.3676544, lng: 44.3580416},
        title: 'second'
    },
    {
        position: {lat: 33.3364, lng: 44.4004},
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
        zoom: 8,
        center: currentlocation
    });
    // var image = 'static/carwash.png'
    // var marker = new google.maps.Marker({
    //     position: currentlocation,
    //     map: map,
    //     icon: image,
    //     tital: "my location"
    // });

    // markers.forEach( function(loc) {
    //     var mark = new google.maps.Marker({
    //         position: loc.position,
    //         title: loc.title,
    //         map: map,
    //     })
    // });
}
