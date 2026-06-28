document.addEventListener("DOMContentLoaded", () => {

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

    // ================= EDIT EMPLOYEE =================

    const editButtons = document.querySelectorAll(".edit-btn");

    editButtons.forEach(button => {

        button.addEventListener("click", function () {

            const employeeId = this.dataset.id;
            const name = this.dataset.name;
            const email = this.dataset.email;
            const designation = this.dataset.designation;

            document.getElementById("editName").value = name;
            document.getElementById("editEmail").value = email;
            document.getElementById("editDesignation").value = designation;

            document.getElementById("editEmployeeForm").action =
                "/manager/edit-employee/" + employeeId;

        });

    });

    // ================= DELETE EMPLOYEE =================

    const deleteButtons = document.querySelectorAll(".delete-btn");

    deleteButtons.forEach(button => {

        button.addEventListener("click", function (e) {

            e.preventDefault();

            const url = this.href;

            Swal.fire({

                title: "Delete Employee?",

                text: "This employee will be permanently deleted.",

                icon: "warning",

                showCancelButton: true,

                confirmButtonColor: "#2E7D32",

                cancelButtonColor: "#dc3545",

                confirmButtonText: "Yes, Delete",

                cancelButtonText: "Cancel"

            }).then((result) => {

                if (result.isConfirmed) {

                    window.location.href = url;

                }

            });

        });

    });

});