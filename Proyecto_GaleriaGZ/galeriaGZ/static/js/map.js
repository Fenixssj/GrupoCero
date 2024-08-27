let map;
function initMap() {
  var coord = {lat: -33.4793861, lng: -70.647373};
  var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 15,
      center: coord 
  });

  var marker = new google.maps.Marker({
      position: coord,
      map: map
  });
}