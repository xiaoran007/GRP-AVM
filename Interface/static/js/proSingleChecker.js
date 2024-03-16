document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("proSingle");
    const quantityInput = document.getElementById("zipcode");
    const modal = new bootstrap.Modal(document.getElementById('myModal'));
    const closeBtn = document.getElementById("closeBtn");

    // Function to validate the input
    function validateInput() {
        const quantity = parseFloat(quantityInput.value);
        if (isNaN(quantity) || quantity > 10) {
            displayCustomAlert();
            return false;
        } else {
            return true;
        }
    }

    // Function to display custom alert
    function displayCustomAlert(err_msg) {
        var errMsg = document.getElementById("errMsg");
        errMsg.textContent = err_msg;
        // var modal = new bootstrap.Modal(document.getElementById('ModalCenter'));
        modal.toggle();
    }

    function hideCustomAlert() {
        console.log('sss')
        // var modal = new bootstrap.Modal(document.getElementById('ModalCenter'));
        modal.hide();
    }

    quantityInput.addEventListener('blur', validateInput);

    closeBtn.addEventListener('click', hideCustomAlert);

});
