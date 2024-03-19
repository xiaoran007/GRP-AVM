document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("normalPro");
    // const modal = new bootstrap.Modal(document.getElementById('myModal'));
    const modal = document.getElementById('myModal');
    const modalBg = document.getElementById("modal_bg");
    const closeBtn = document.getElementById("closeBtn");
    const errMsg = document.getElementById("errMsg");

    closeBtn.addEventListener('click', hideCustomAlert);

    const viewInput = document.getElementById("viewnum");
    viewInput.addEventListener('blur', function() {
        validateView(true, viewInput.value);
    });
    function validateView(inside, value) {
        if (value === "") {
            return false;
        }
        const value_num = Number(value);
        console.log(value_num)
        if (isNaN(value_num) || (!Number.isInteger(value_num)) || value_num < 0) {
            if (inside) {
                displayCustomAlert("Please enter a valid viewed times.");
            }
            return false;
        }
        else {
            return true;
        }
    }


    const gradeInput = document.getElementById("gradenum");
    gradeInput.addEventListener('blur', function() {
        validateGrade(true, gradeInput.value);
    });
    function validateGrade(inside, value) {
        if (value === "") {
            return false;
        }
        const value_num = Number(value);
        console.log(value_num)
        if (isNaN(value_num) || (!Number.isInteger(value_num)) || (value_num < 1 && value_num !== -1) || value_num > 13) {
            if (inside) {
                displayCustomAlert("Please enter a valid grade (1 - 13 or -1).");
            }
            return false;
        }
        else {
            return true;
        }
    }


    function validateAll() {
        return validateView(false, viewInput.value) && validateGrade(false, gradeInput.value);
    }


    function displayCustomAlert(err_msg) {
        console.log("display");
        errMsg.textContent = err_msg;
        document.body.className = "modal-open";
        modal.className="modal fade in";
        modal.style.display = "block";
        modalBg.className = "modal-backdrop fade in";

    }

    function hideCustomAlert() {
        console.log("hide");
        modal.className="modal fade";
        modal.style.display = "none";
        modalBg.className = "";
        document.body.className = "";
    }

    function validateCondition() {
        const conditions = document.getElementsByName("condition");
        console.log(conditions);
        for (let i = 0; i < conditions.length; i++) {
            console.log(conditions[i], conditions[i].checked);
            if (conditions[i].checked) {
                return true;
            }
        }
        return false;
    }


    form.addEventListener("submit", function(event) {
        if (!validateAll()) {
            event.preventDefault();
            displayCustomAlert("Please check your input (make sure input all blocks).");
        }
        if (!validateCondition()) {
            event.preventDefault();
            displayCustomAlert("Please check condition.");
        }
    });

});
