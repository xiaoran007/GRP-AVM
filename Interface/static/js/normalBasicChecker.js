/*Copyright (c) 2024 Tangtangfang Fang*/

/*All rights reserved.*/

/*This file is part of AVM-GRP.*/

/*AVM-GRP is distributed under the GPLv3 License.*/
/*See the LICENSE file at the top level of the distribution for details.*/


document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("normalBasic");
    // const modal = new bootstrap.Modal(document.getElementById('myModal'));
    const modal = document.getElementById('myModal');
    const modalBg = document.getElementById("modal_bg");
    const closeBtn = document.getElementById("closeBtn");
    const errMsg = document.getElementById("errMsg");

    closeBtn.addEventListener('click', hideCustomAlert);

    const zipcodeInput = document.getElementById("zipcode");
    zipcodeInput.addEventListener('blur', function() {
        validateZipcode(true, zipcodeInput.value);
    });
    function validateZipcode(inside, value) {
        const value_num = Number(value);
        console.log(value_num)
        if (isNaN(value_num) || (!Number.isInteger(value_num)) || value_num < 0) {
            if (inside) {
                displayCustomAlert("Please enter a valid zipcode.");
            }
            return false;
        }
        else {
            return true;
        }
    }


    const latInput = document.getElementById("latitude");
    latInput.addEventListener('blur', function() {
        validateLat(true, latInput.value);
    });
    function validateLat(inside, value) {
        if (value === "") {
            return false;
        }
        const value_num = Number(value);
        console.log(value_num)
        if (isNaN(value_num) || value_num < -90 || value_num > 90) {
            if (inside) {
                displayCustomAlert("Please enter a valid latitude (between -90 and 90).");
            }
            return false;
        }
        else {
            return true;
        }
    }


    const longInput = document.getElementById("longitude");
    longInput.addEventListener('blur', function() {
        validateLong(true, longInput.value);
    });
    function validateLong(inside, value) {
        if (value === "") {
            return false;
        }
        const value_num = Number(value);
        console.log(value_num)
        if (isNaN(value_num) || value_num < -180 || value_num > 180) {
            if (inside) {
                displayCustomAlert("Please enter a valid longitude (between -180 and 180).");
            }
            return false;
        }
        else {
            return true;
        }
    }


    const bedroomsInput = document.getElementById("bedrooms");
    bedroomsInput.addEventListener('blur', function() {
        validateBedrooms(true, bedroomsInput.value);
    });
    function validateBedrooms(inside, value) {
        if (value === "") {
            return false;
        }
        const value_num = Number(value);
        console.log(value_num)
        if (isNaN(value_num) || (!Number.isInteger(value_num)) || value_num < 1) {
            if (inside) {
                displayCustomAlert("Please enter a valid bedrooms number.");
            }
            return false;
        }
        else {
            return true;
        }
    }


    const bathroomsInput = document.getElementById("bathrooms");
    bathroomsInput.addEventListener('blur', function() {
        validateBathrooms(true, bathroomsInput.value);
    });
    function validateBathrooms(inside, value) {
        if (value === "") {
            return false;
        }
        const value_num = Number(value);
        console.log(value_num)
        if (isNaN(value_num) || (!Number.isInteger(value_num)) || value_num < 0) {
            if (inside) {
                displayCustomAlert("Please enter a valid bathrooms number.");
            }
            return false;
        }
        else {
            return true;
        }
    }


    const sqft_livingInput = document.getElementById("sqft_living");
    sqft_livingInput.addEventListener('blur', function() {
        validateSqlv(true, sqft_livingInput.value);
    });
    function validateSqlv(inside, value) {
        if (value === "") {
            return false;
        }
        const value_num = Number(value);
        console.log(value_num)
        if (isNaN(value_num) || value_num < 0) {
            if (inside) {
                displayCustomAlert("Please enter a valid living area size.");
            }
            return false;
        }
        else {
            return true;
        }
    }


    const sqft_lotInput = document.getElementById("sqft_lot");
    sqft_lotInput.addEventListener('blur', function() {
        validateSqlot(true, sqft_lotInput.value);
    });
    function validateSqlot(inside, value) {
        if (value === "") {
            return false;
        }
        const value_num = Number(value);
        console.log(value_num)
        if (isNaN(value_num) || value_num < 0) {
            if (inside) {
                displayCustomAlert("Please enter a valid lot area size.");
            }
            return false;
        }
        else {
            return true;
        }
    }


    const floorsInput = document.getElementById("floors");
    floorsInput.addEventListener('blur', function() {
        validateFloors(true, floorsInput.value);
    });
    function validateFloors(inside, value) {
        if (value === "") {
            return false;
        }
        const value_num = Number(value);
        console.log(value_num)
        if (isNaN(value_num) || value_num < 0) {
            if (inside) {
                displayCustomAlert("Please enter a valid floors.");
            }
            return false;
        }
        else {
            return true;
        }
    }


    const sqft_aboveInput = document.getElementById("sqft_above");
    sqft_aboveInput.addEventListener('blur', function() {
        validateSqab(true, sqft_aboveInput.value);
    });
    function validateSqab(inside, value) {
        if (value === "") {
            return false;
        }
        const value_num = Number(value);
        console.log(value_num)
        if (isNaN(value_num) || value_num < 0) {
            if (inside) {
                displayCustomAlert("Please enter a valid above basement area size.");
            }
            return false;
        }
        else {
            return true;
        }
    }


    const sqft_basementInput = document.getElementById("sqft_basement");
    sqft_basementInput.addEventListener('blur', function() {
        validateSqbase(true, sqft_basementInput.value);
    });
    function validateSqbase(inside, value) {
        if (value === "") {
            return false;
        }
        const value_num = Number(value);
        console.log(value_num)
        if (isNaN(value_num) || value_num < 0) {
            if (inside) {
                displayCustomAlert("Please enter a valid basement area size.");
            }
            return false;
        }
        else {
            return true;
        }
    }


    const yr_builtInput = document.getElementById("yr_built");
    yr_builtInput.addEventListener('blur', function() {
        validateYr(true, yr_builtInput.value);
    });
    function validateYr(inside, value) {
        if (value === "") {
            return false;
        }
        const value_num = Number(value);
        console.log(value_num)
        if (isNaN(value_num) || (!Number.isInteger(value_num)) || value_num < 0 || value_num > 2015) {
            if (inside) {
                displayCustomAlert("Please enter a valid built year (before 2015).");
            }
            return false;
        }
        else {
            return true;
        }
    }


    const yr_renovatedInput = document.getElementById("yr_renovated");
    yr_renovatedInput.addEventListener('blur', function() {
        validateRe(true, yr_renovatedInput.value);
    });
    function validateRe(inside, value) {
        if (value === "") {
            return false;
        }
        const value_num = Number(value);
        console.log(value_num)
        if (isNaN(value_num) || (!Number.isInteger(value_num)) || value_num < 0 || value_num > 2015) {
            if (inside) {
                displayCustomAlert("Please enter a valid renovated year (before 2015).");
            }
            return false;
        }
        else if (Number(yr_builtInput.value) > Number(value)) {
            if (Number(value) === 0) {
                return true;
            }
            if (inside) {
                displayCustomAlert("Please enter a valid renovated year (after built year).");
            }
            return false;
        }
        else {
            return true;
        }
    }


    const sqft_living15Input = document.getElementById("sqft_living15");
    sqft_living15Input.addEventListener('blur', function() {
        validateSqlv15(true, sqft_living15Input.value);
    });
    function validateSqlv15(inside, value) {
        if (value === "") {
            return false;
        }
        const value_num = Number(value);
        console.log(value_num)
        if (isNaN(value_num) || value_num < 0) {
            if (inside) {
                displayCustomAlert("Please enter a valid living area size (2015).");
            }
            return false;
        }
        else {
            return true;
        }
    }


    const sqft_lot15Input = document.getElementById("sqft_lot15");
    sqft_lot15Input.addEventListener('blur', function() {
        validateSqlot15(true, sqft_lot15Input.value);
    });
    function validateSqlot15(inside, value) {
        if (value === "") {
            return false;
        }
        const value_num = Number(value);
        console.log(value_num)
        if (isNaN(value_num) || value_num < 0) {
            if (inside) {
                displayCustomAlert("Please enter a valid lot area size (2015).");
            }
            return false;
        }
        else {
            return true;
        }
    }


    function validateAll() {
        return validateZipcode(false, zipcodeInput.value) && validateLat(false, latInput.value)
        && validateLong(false, longInput.value)
        && validateBedrooms(false, bedroomsInput.value) && validateBathrooms(false, bathroomsInput.value)
        && validateFloors(false, floorsInput.value) && validateYr(false, yr_builtInput.value)
        && validateRe(false, yr_renovatedInput.value) && validateSqlv(false, sqft_livingInput.value)
        && validateSqlot(false, sqft_lotInput.value) && validateSqab(false, sqft_aboveInput.value)
        && validateSqbase(false, sqft_basementInput.value)
        && validateSqlv15(false, sqft_living15Input.value) && validateSqlot15(false, sqft_lot15Input.value);

    }


    function displayCustomAlert(err_msg) {
        console.log("display");
        errMsg.textContent = err_msg;
        // modal.show();
        console.log(modal)
        // $('#myModal').modal('show')
        document.body.className = "modal-open";
        modal.className="modal fade in";
        modal.style.display = "block";
        modalBg.className = "modal-backdrop fade in";

    }

    function hideCustomAlert() {
        console.log("hide");
        // $('#myModal').modal('hide')
        modal.className="modal fade";
        modal.style.display = "none";
        modalBg.className = "";
        document.body.className = "";
    }



    form.addEventListener("submit", function(event) {
        if (!validateAll()) {
            event.preventDefault();
            displayCustomAlert("Please check your input (make sure input all blocks).");
        }
    });

});
