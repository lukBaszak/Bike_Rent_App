    document.addEventListener('DOMContentLoaded', function(){
        if (document.querySelectorAll('#map').length >0)
        {
            if(document.querySelector('html').lang) {
                lang = document.querySelector('html').lang
            }
            else
                lang ='en';

            var js_file = document.createElement('script');
            js_file.type = 'text/javascript';
            js_file.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyCxn0UQot5aqIKu3TEoYfObTWNTlyemRwE&callback=initMap&signed_in=true&language=' + lang;
            document.getElementsByTagName('head')[0].appendChild(js_file);
        }
    });

    var map;

    function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
            center: {lat: -34.397, lng: 150.644},
            zoom: 8
        });

       fetch('/stations/', {
           method: 'get',
           credentials: 'same-origin',
           headers: {
        'X-Requested-With': 'XMLHttpRequest',
        "Accept": "application/json",
        "Content-Type": "application/json"
            },
       })
           .then(function(response){
               return response.json()})
           .then(plotMarkers);


    }
    var markers;
    var bounds;

    function plotMarkers(m) {
        markers = [];
        bounds = new google.maps.LatLngBounds();

        m.forEach(function(marker){
            var content;

            var position = new google.maps.LatLng(marker.latitude, marker.longitude);
            var mark = new google.maps.Marker({
                  position: position,
                  map: map,
                });


            markers.push(mark);

            bounds.extend(position)
        });

        map.fitBounds(bounds)
    }
