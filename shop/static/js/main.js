
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

// Back to the top button-The code below is adapted from the Traversy Media you tube video project :'myTunes Site','Responsive Landing Page using HTML and CSS (A little jQuery - published on 19th August 2018)

$(document).ready(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 750) {
            $('#topBtn').fadeIn();

        }
        else {
            $("#topBtn").fadeOut();
        }
    });
    // scroll body to 0px on click
    $('#topBtn').click(function() {
        $('body,html').animate({
                scrollTop: 0
            },
            100
        );
        return false;
    });
});

// Fade Out JS for Alerts

setTimeout(function(){
    $('#message').fadeOut('fast');
}, 3000);

//  Recaptcha JS
grecaptcha.ready(function() {
    // 4
    $('#contactform').submit(function(e){
        var form = this;
        // 5
        e.preventDefault()
        grecaptcha.execute('reCAPTCHA_site_key', {action: 'contactform'}).then(function(token) {
            // 6
            $('#recaptcha').val(token)
            // 7
            form.submit()
        });
    })
});