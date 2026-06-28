document.addEventListener("DOMContentLoaded", () => {

    // ================= DISTRICT DROPDOWN =================

    const state = document.getElementById("state");
    const district = document.getElementById("district");

    if (state) {

        state.addEventListener("change", function () {

            district.innerHTML =
                '<option selected disabled>Loading...</option>';

            fetch(`/employee/get-districts/${this.value}`)

                .then(response => response.json())

                .then(data => {

                    district.innerHTML =
                        '<option selected disabled>Select District</option>';

                    data.forEach(item => {

                        district.innerHTML +=
                            `<option value="${item.id}">
                                ${item.district_name}
                            </option>`;

                    });

                });

        });

    }

    // ================= PRICE & TOTAL =================

    const fertilizer = document.getElementById("fertilizer");
    const price = document.getElementById("price");
    const quantity = document.getElementById("quantity");
    const total = document.getElementById("totalAmount");

    function calculateTotal() {

        const qty = parseFloat(quantity?.value) || 0;

        const rate = parseFloat(price?.value) || 0;

        total.value = (qty * rate).toFixed(2);

    }

    if (fertilizer) {

        fertilizer.addEventListener("change", function () {

            const selected =
                this.options[this.selectedIndex];

            price.value =
                selected.dataset.price || "";

            calculateTotal();

        });

    }

    if (quantity) {

        quantity.addEventListener(
            "input",
            calculateTotal
        );

    }

    // ================= SEARCH =================

    const searchInput = document.getElementById("searchInput");

    if (searchInput) {

        searchInput.addEventListener("keyup", function () {

            const value = this.value.toLowerCase();

            document.querySelectorAll("tbody tr").forEach(row => {

                row.style.display = row.innerText
                    .toLowerCase()
                    .includes(value)
                    ? ""
                    : "none";

            });

        });

    }

    // ================= DELETE SALE =================

    document.querySelectorAll(".delete-sale-btn").forEach(button => {

        button.addEventListener("click", function (e) {

            e.preventDefault();

            const url = this.href;

            Swal.fire({

                title: "Delete Sales Record?",

                text: "This record will be permanently deleted.",

                icon: "warning",

                showCancelButton: true,

                confirmButtonColor: "#2E7D32",

                cancelButtonColor: "#d33",

                confirmButtonText: "Delete"

            }).then((result) => {

                if (result.isConfirmed) {

                    window.location.href = url;

                }

            });

        });

    });

});