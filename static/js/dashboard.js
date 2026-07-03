document.addEventListener("DOMContentLoaded", function () {

    // ==========================================
    // COUNTER ANIMATION
    // ==========================================

    const counters = document.querySelectorAll("h2, h3");

    counters.forEach(counter => {

        const text = counter.innerText
            .replace(/,/g, "")
            .replace("₹", "")
            .replace("%", "")
            .trim();

        const target = parseFloat(text);

        if (isNaN(target)) return;

        let current = 0;

        const increment = target / 60;

        function updateCounter() {

            if (current < target) {

                current += increment;

                if (target >= 1000) {

                    counter.innerText =
                        Math.floor(current).toLocaleString();

                } else {

                    counter.innerText =
                        Math.floor(current);

                }

                requestAnimationFrame(updateCounter);

            } else {

                if (text.includes(".")) {

                    counter.innerText = target.toFixed(2);

                } else if (target >= 1000) {

                    counter.innerText =
                        target.toLocaleString();

                } else {

                    counter.innerText = target;

                }

            }

        }

        updateCounter();

    });


    // ==========================================
    // CARD HOVER EFFECT
    // ==========================================

    document.querySelectorAll(".dashboard-card").forEach(card => {

        card.addEventListener("mouseenter", function () {

            this.style.transform = "translateY(-8px)";

            this.style.transition = "0.35s";

        });

        card.addEventListener("mouseleave", function () {

            this.style.transform = "translateY(0px)";

        });

    });


    // ==========================================
    // BUTTON RIPPLE EFFECT
    // ==========================================

    document.querySelectorAll(".btn").forEach(btn => {

        btn.addEventListener("click", function () {

            this.style.transform = "scale(.96)";

            setTimeout(() => {

                this.style.transform = "";

            }, 120);

        });

    });


    // ==========================================
    // TABLE ROW HIGHLIGHT
    // ==========================================

    document.querySelectorAll("tbody tr").forEach(row => {

        row.addEventListener("mouseenter", function () {

            this.style.transition = ".25s";

            this.style.transform = "scale(1.01)";

        });

        row.addEventListener("mouseleave", function () {

            this.style.transform = "scale(1)";

        });

    });


    // ==========================================
    // FADE-IN ANIMATION
    // ==========================================

    document.querySelectorAll(".dashboard-card").forEach((card, index) => {

        card.style.opacity = "0";

        card.style.transform = "translateY(25px)";

        setTimeout(() => {

            card.style.transition = ".5s";

            card.style.opacity = "1";

            card.style.transform = "translateY(0px)";

        }, index * 120);

    });

});