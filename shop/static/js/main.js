
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

// carousel slider

$(document).ready(function() {
    $("#myCarousel").on("slide.bs.carousel", function(e) {
      var $e = $(e.relatedTarget);
      var idx = $e.index();
      var itemsPerSlide = 3;
      var totalItems = $(".carousel-item").length;
  
      if (idx >= totalItems - (itemsPerSlide - 1)) {
        var it = itemsPerSlide - (totalItems - idx);
        for (var i = 0; i < it; i++) {
          // append slides to end
          if (e.direction == "left") {
            $(".carousel-item")
              .eq(i)
              .appendTo(".carousel-inner");
          } else {
            $(".carousel-item")
              .eq(0)
              .appendTo($(this).find(".carousel-inner"));
          }
        }
      }
    });
  });
