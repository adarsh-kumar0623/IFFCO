// ======================================================
// MONTHLY REVENUE
// ======================================================

const monthlyCanvas = document.getElementById("monthlySalesChart");

if (monthlyCanvas) {

    new Chart(monthlyCanvas, {

        type: "line",

        data: {

            labels: monthLabels,

            datasets: [

                {

                    label: "Revenue",

                    data: monthValues,

                    borderColor: "#16A34A",

                    backgroundColor: "rgba(22,163,74,.15)",

                    fill: true,

                    tension: .4

                }

            ]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    display: false

                }

            }

        }

    });

}


// ======================================================
// STATE REVENUE
// ======================================================

const stateCanvas = document.getElementById("stateSalesChart");

if (stateCanvas) {

    new Chart(stateCanvas, {

        type: "bar",

        data: {

            labels: stateLabels,

            datasets: [

                {

                    label: "Revenue",

                    data: stateValues,

                    backgroundColor: [

                        "#16A34A",

                        "#22C55E",

                        "#15803D",

                        "#4ADE80",

                        "#65A30D"

                    ]

                }

            ]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    display: false

                }

            }

        }

    });

}


// ======================================================
// TOP FERTILIZER
// ======================================================

const fertilizerCanvas = document.getElementById("fertilizerChart");

if (fertilizerCanvas) {

    new Chart(fertilizerCanvas, {

        type: "doughnut",

        data: {

            labels: fertilizerLabels,

            datasets: [

                {

                    data: fertilizerValues,

                    backgroundColor: [

                        "#16A34A",

                        "#22C55E",

                        "#0EA5E9",

                        "#F59E0B",

                        "#DC2626"

                    ]

                }

            ]

        },

        options: {

            responsive: true

        }

    });

}


// ======================================================
// TOP EMPLOYEE
// ======================================================

const employeeCanvas = document.getElementById("employeeChart");

if (employeeCanvas) {

    new Chart(employeeCanvas, {

        type: "bar",

        data: {

            labels: employeeLabels,

            datasets: [

                {

                    label: "Sales",

                    data: employeeValues,

                    backgroundColor: "#16A34A"

                }

            ]

        },

        options: {

            responsive: true,

            indexAxis: "y",

            plugins: {

                legend: {

                    display: false

                }

            }

        }

    });

}
// ======================================================
// FORECAST CHART
// ======================================================

const forecastCanvas = document.getElementById("forecastChart");

if (forecastCanvas && typeof predicted_demand !== "undefined") {

    new Chart(forecastCanvas, {

        type: "line",

        data: {

            labels: [

                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Forecast"

            ],

            datasets: [

                {

                    label: "Demand Forecast",

                    data: [

                        120,
                        180,
                        220,
                        260,
                        300,
                        predicted_demand

                    ],

                    borderColor: "#16A34A",

                    backgroundColor: "rgba(22,163,74,.15)",

                    fill: true,

                    tension: .4,

                    borderWidth: 3

                }

            ]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {

                    display: false

                }

            },

            scales: {

                y: {

                    beginAtZero: true

                }

            }

        }

    });

}