

function onGeoOk(position) {
    
}

function onGeoError() {
    alert("Can't find you. No weather for you.")
}


navigator.geolocation.getCurrentPosition(onGeoError, onGeoOk);;
