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

if (forecastCanvas) {

    let labels = [];

    let values = [];

    if (historyLabels.length > 0) {

        labels = [...historyLabels];

        values = [...historyValues];

    }

    if (predicted_demand > 0) {

        labels.push("Prediction");

        values.push(predicted_demand);

    }

    new Chart(forecastCanvas, {

        type: "line",

        data: {

            labels: labels,

            datasets: [

                {

                    label: "Historical + Predicted Demand",

                    data: values,

                    borderColor: "#16A34A",

                    backgroundColor: "rgba(22,163,74,0.12)",

                    borderWidth: 4,

                    pointRadius: 6,

                    pointHoverRadius: 8,

                    pointBackgroundColor: [

                        ...new Array(values.length - 1).fill("#16A34A"),

                        "#DC2626"

                    ],

                    pointBorderColor: "#ffffff",

                    pointBorderWidth: 2,

                    fill: true,

                    tension: 0.35

                }

            ]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            interaction: {

                intersect: false,

                mode: "index"

            },

            plugins: {

                legend: {

                    display: true,

                    position: "top"

                },

                tooltip: {

                    callbacks: {

                        label: function(context) {

                            return " Demand : " + context.parsed.y + " Bags";

                        }

                    }

                }

            },

            scales: {

                y: {

                    beginAtZero: true,

                    title: {

                        display: true,

                        text: "Demand (Bags)"

                    }

                },

                x: {

                    title: {

                        display: true,

                        text: "Months"

                    }

                }

            }

        }

    });

}