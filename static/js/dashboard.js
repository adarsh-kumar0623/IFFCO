document.addEventListener("DOMContentLoaded", () => {

    // Dashboard Counter Animation
    const counters = document.querySelectorAll(".counter");

    counters.forEach(counter => {

        const target = Number(counter.getAttribute("data-target")) || 0;

        let count = 0;

        const speed = Math.max(1, Math.ceil(target / 100));

        const updateCounter = () => {

            if (count < target) {

                count += speed;

                if (count > target) count = target;

                counter.innerText = count.toLocaleString();

                requestAnimationFrame(updateCounter);

            }

        };

        updateCounter();

    });

    // Current Date
    const dateBox = document.getElementById("currentDate");

    if (dateBox) {

        const today = new Date();

        dateBox.innerHTML = today.toLocaleDateString("en-IN", {
            weekday: "long",
            day: "numeric",
            month: "long",
            year: "numeric"
        });

    }

});