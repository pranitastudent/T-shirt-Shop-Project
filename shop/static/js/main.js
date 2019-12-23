
// Year-  Code Taken from Brad Traversy's Course Python Django to Dev (Nov 2018)
const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// End of Code taken

// Map

function initMap() {
    // Your location
    const loc = { lat: 51.46759, lng: -0.3618 };
    // Centered map on location
    const map = new google.maps.Map(document.querySelector(".map"), {
        zoom: 15,
        center: loc
    });
    // The marker, positioned at location
    const marker = new google.maps.Marker({ position: loc, map: map });
}



  