document.addEventListener("DOMContentLoaded", function () {

    console.log("IFFCO Fertilizer Demand Forecasting System Loaded");

    // Active Navbar Link
    const currentPath = window.location.pathname;

    document.querySelectorAll(".nav-link").forEach(link => {
        if (link.getAttribute("href") === currentPath) {
            link.classList.add("active");
        }
    });

    // Confirm Delete
    document.querySelectorAll(".delete-btn").forEach(button => {

        button.addEventListener("click", function (e) {

            if (!confirm("Are you sure you want to delete this record?")) {
                e.preventDefault();
            }

        });

    });

});