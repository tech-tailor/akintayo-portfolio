$(document).ready(function(){
    alert('yes')
    $("#getLocationBtn").click(function(){
        if ("geolocation" in navigator) {
            navigator.geolocation.getCurrentPosition(function(position) {
                var latitude = position.coords.latitude;
                var longitude = position.coords.longitude;
                alert(latitude)
                alert(longitude)
            },
            function(error) {
                // Location access denied or error occurred
                if (error.code === error.PERMISSION_DENIED) {
                    // Prompt the user to allow location access
                    const allowLocation = confirm("Please allow access to your location to use this service. Do you want to enable location access?");
                    if (allowLocation) {
                        // Redirect user to browser settings
                        window.location.href = "chrome://settings/content/location";
                    } else {
                        // Handle denial gracefully
                        console.log("User denied location access.");
                    }
                } else {
                    // Handle other errors
                    console.error("Error getting location:", error);
                }
            })
        } else {
            alert('no geolocation')
        }
    
    });

});