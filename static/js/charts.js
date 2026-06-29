// ======================================================
// MONTHLY REVENUE CHART
// ======================================================

const monthlyCanvas = document.getElementById("monthlySalesChart");

if (monthlyCanvas && typeof monthLabels !== "undefined") {

    new Chart(monthlyCanvas, {

        type: "line",

        data: {

            labels: monthLabels,

            datasets: [

                {

                    label: "Monthly Revenue",

                    data: monthValues,

                    borderColor: "#16A34A",

                    backgroundColor: "rgba(22,163,74,0.12)",

                    borderWidth: 3,

                    fill: true,

                    tension: 0.35,

                    pointRadius: 5,

                    pointHoverRadius: 8,

                    pointBackgroundColor: "#16A34A"

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



// ======================================================
// STATE WISE SALES
// ======================================================

const stateCanvas = document.getElementById("stateSalesChart");

if (stateCanvas && typeof stateLabels !== "undefined") {

    new Chart(stateCanvas, {

        type: "bar",

        data: {

            labels: stateLabels,

            datasets: [

                {

                    label: "Revenue",

                    data: stateValues,

                    borderRadius: 10,

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
// ======================================================
// TOP FERTILIZER
// ======================================================

const fertilizerCanvas = document.getElementById("fertilizerChart");

if (fertilizerCanvas && typeof fertilizerLabels !== "undefined") {

    new Chart(fertilizerCanvas, {

        type: "doughnut",

        data: {

            labels: fertilizerLabels,

            datasets: [{

                data: fertilizerValues,

                backgroundColor: [

                    "#16A34A",
                    "#22C55E",
                    "#0EA5E9",
                    "#F59E0B",
                    "#DC2626"

                ]

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {

                    position: "bottom"

                }

            }

        }

    });

}



// ======================================================
// TOP EMPLOYEE
// ======================================================

const employeeCanvas = document.getElementById("employeeChart");

if (employeeCanvas && typeof employeeLabels !== "undefined") {

    new Chart(employeeCanvas, {

        type: "bar",

        data: {

            labels: employeeLabels,

            datasets: [{

                label: "Sales",

                data: employeeValues,

                backgroundColor: "#16A34A",

                borderRadius: 10

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            indexAxis: "y",

            plugins: {

                legend: {

                    display: false

                }

            },

            scales: {

                x: {

                    beginAtZero: true

                }

            }

        }

    });

}



// ======================================================
// AI FORECAST CHART
// ======================================================

const forecastCanvas = document.getElementById("forecastChart");

if (

    forecastCanvas &&

    typeof historyLabels !== "undefined" &&

    typeof historyValues !== "undefined"

) {

    let labels = [...historyLabels];

    let values = [...historyValues];

    if (predicted_demand > 0) {

        labels.push("Prediction");

        values.push(predicted_demand);

    }

    const pointColors = values.map((_, index) =>

        index === values.length - 1

            ? "#DC2626"

            : "#16A34A"

    );

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

                    borderWidth: 3,

                    fill: true,

                    tension: 0.4,

                    pointRadius: 6,

                    pointHoverRadius: 8,

                    pointBackgroundColor: pointColors,

                    pointBorderColor: "#ffffff",

                    pointBorderWidth: 2

                }

            ]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            interaction: {

                mode: "index",

                intersect: false

            },

            plugins: {

                legend: {

                    display: true,

                    position: "top"

                },

                tooltip: {

                    callbacks: {

                        label: function(context) {

                            return "Demand : " +

                                   context.parsed.y +

                                   " Bags";

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