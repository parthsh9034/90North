window.addEventListener('resize', function() {
    var width = window.innerWidth;

    if (width >= 992 && width <= 1600) {
        document.body.style.zoom = "0.1";
    } else if (width >= 700 && width <= 767) {
        document.body.style.zoom = "0.2";
    } else if (width >= 600 && width <= 700) {
        document.body.style.width = "75%";
    } else if (width <= 600) {
        document.body.style.width = "50%";
    } else {
        document.body.style.zoom = "1"; // Reset zoom for other screen sizes
        document.body.style.width = "auto"; // Reset width for other screen sizes
    }
});