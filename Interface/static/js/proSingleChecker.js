document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("proSingle");
    const zipcodeInput = document.getElementById("zipcode");
    const modal = new bootstrap.Modal(document.getElementById('myModal'));
    const closeBtn = document.getElementById("closeBtn");
    const errMsg = document.getElementById("errMsg");

    function validateZipcode(inside) {
        const zipcode = Number(zipcodeInput.value);
        console.log(zipcode)
        if (isNaN(zipcode) || (!Number.isInteger(zipcode)) || zipcode < 0) {
            if (inside) {
                displayCustomAlert("Please enter a valid zipcode.");
            }
            return false;
        }
        else {
            return true;
        }
    }

    zipcodeInput.addEventListener('blur', function() {
        validateZipcode(true);
    });

    // Function to display custom alert
    function displayCustomAlert(err_msg) {
        errMsg.textContent = err_msg;
        modal.toggle();
    }

    function hideCustomAlert() {
        modal.hide();
    }

    closeBtn.addEventListener('click', hideCustomAlert);

    form.addEventListener("submit", function(event) {
        if (!validateInput()) {
            event.preventDefault(); // Prevent form submission if input is invalid
        }
    });

});
