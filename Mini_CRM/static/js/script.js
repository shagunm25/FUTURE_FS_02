// =========================
// PAGE LOAD ANIMATION
// =========================

window.addEventListener("load", () => {

    document.body.style.opacity = "1";

});

// =========================
// DELETE CONFIRMATION
// =========================

const deleteButtons =
    document.querySelectorAll(".delete-btn");

deleteButtons.forEach(button => {

    button.addEventListener("click", function (e) {

        const confirmDelete =
            confirm(
                "Are you sure you want to delete this customer?"
            );

        if (!confirmDelete) {

            e.preventDefault();

        }

    });

});

// =========================
// SEARCH INPUT FOCUS EFFECT
// =========================

const searchInput =
    document.querySelector(
        ".search-form input"
    );

if (searchInput) {

    searchInput.addEventListener(
        "focus",
        () => {

            searchInput.style.borderColor =
                "#f97316";

        }
    );

    searchInput.addEventListener(
        "blur",
        () => {

            searchInput.style.borderColor =
                "#334155";

        }
    );

}

// =========================
// TABLE ROW HOVER EFFECT
// =========================

const tableRows =
    document.querySelectorAll(
        "tbody tr"
    );

tableRows.forEach(row => {

    row.addEventListener(
        "mouseenter",
        () => {

            row.style.transform =
                "scale(1.01)";

        }
    );

    row.addEventListener(
        "mouseleave",
        () => {

            row.style.transform =
                "scale(1)";

        }
    );

});

// =========================
// INPUT FIELD ANIMATION
// =========================

const inputs =
    document.querySelectorAll(
        "input"
    );

inputs.forEach(input => {

    input.addEventListener(
        "focus",
        () => {

            input.style.boxShadow =
                "0 0 10px rgba(249,115,22,.3)";

        }
    );

    input.addEventListener(
        "blur",
        () => {

            input.style.boxShadow =
                "none";

        }
    );

});

// =========================
// DASHBOARD CARD EFFECT
// =========================

const statCard =
    document.querySelector(
        ".stat-card"
    );

if (statCard) {

    statCard.addEventListener(
        "mouseenter",
        () => {

            statCard.style.transform =
                "translateY(-5px)";

        }
    );

    statCard.addEventListener(
        "mouseleave",
        () => {

            statCard.style.transform =
                "translateY(0px)";

        }
    );

}

// =========================
// BUTTON HOVER EFFECT
// =========================

const buttons =
    document.querySelectorAll(
        "button, .nav-btn, .save-btn, .back-btn"
    );

buttons.forEach(button => {

    button.addEventListener(
        "mouseenter",
        () => {

            button.style.transition =
                "0.3s";

        }
    );

});

// =========================
// AUTO FOCUS SEARCH
// =========================

if (searchInput) {

    searchInput.focus();

}

// =========================
// CONSOLE MESSAGE
// =========================

console.log(
    "Mini CRM Loaded Successfully"
);