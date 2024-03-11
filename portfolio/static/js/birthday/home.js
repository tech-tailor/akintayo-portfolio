$( document ).ready(function() {
    // Add smooth scrolling to all links
    $("a").on('click', function(event) {
        // Make sure this.hash has a value before overriding default behavior
        if (this.hash !== "") {
        // Prevent default anchor click behavior
        event.preventDefault();
        // Store hash
        var hash = this.hash;
        // Using jQuery's animate() method to add smooth page scroll
        // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
        $('html, body').animate({
            scrollTop: $(hash).offset().top
        }, 800, function(){
            // Add hash (#) to URL when done scrolling (default click behavior)
            window.location.hash = hash;
        });
        } // End if
    });

    // countdown date and time
    var countDownDate = new Date("March 15, 2024 23:59:59").getTime();

    // Update the countdown every 1 second
    var countdown = setInterval(function() {
        // Get the current date and time
        var now = new Date().getTime();

        // Find the distance between now and the countdown date
        var distance = countDownDate - now;

        // Calculate days, hours, minutes, and seconds
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the countdown in the console
        $('#days').text(days);
        $('#hours').text(hours);
        $('#minutes').text(minutes);
        $('#seconds').text(seconds);

        // If the countdown is finished, clear the interval
        if (distance < 0) {
            clearInterval(countdown);
            console.log("Countdown finished!");
        }
    }, 1000);
});

