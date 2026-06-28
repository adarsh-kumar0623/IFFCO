from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    url_for,
    request,
    flash,
    Response
)

import csv
from io import StringIO

from models.manager import Manager
from models.dashboard import (
    get_dashboard_summary,
    monthly_sales_chart,
    state_sales_chart,
    fertilizer_sales_chart,
    employee_sales_chart
)

manager = Blueprint("manager", __name__)


# ================= AUTH =================

def manager_required():
    return session.get("user_role") == "manager"


# ================= DASHBOARD =================

@manager.route("/manager/dashboard")
def dashboard():

    if not manager_required():
        return redirect(url_for("auth.login"))

    summary = get_dashboard_summary()

    recent_sales = Manager.get_recent_sales(10)

    month_labels, month_values = monthly_sales_chart()

    state_labels, state_values = state_sales_chart()

    return render_template(

        "manager/dashboard.html",

        summary=summary,

        recent_sales=recent_sales,

        month_labels=month_labels,

        month_values=month_values,

        state_labels=state_labels,

        state_values=state_values

    )


# ================= EMPLOYEES =================

@manager.route("/manager/employees", methods=["GET", "POST"])
def employees():

    if not manager_required():
        return redirect(url_for("auth.login"))

    if request.method == "POST":

        success = Manager.add_employee(

            request.form["employee_id"],
            request.form["name"],
            request.form["email"],
            request.form["designation"],
            request.form["password"]

        )

        if success:

            flash(
                "Employee added successfully.",
                "success"
            )

        else:

            flash(
                "Employee ID or Email already exists.",
                "danger"
            )

        return redirect(
            url_for("manager.employees")
        )

    employees = Manager.get_all_employees()

    return render_template(

        "manager/employees.html",

        employees=employees,

        total=len(employees)

    )


# ================= EDIT EMPLOYEE =================

@manager.route("/manager/edit-employee/<employee_id>", methods=["POST"])
def edit_employee(employee_id):

    if not manager_required():
        return redirect(url_for("auth.login"))

    success = Manager.update_employee(

        employee_id,

        request.form["name"],

        request.form["email"],

        request.form["designation"]

    )

    if success:

        flash(
            "Employee updated successfully.",
            "success"
        )

    else:

        flash(
            "Unable to update employee.",
            "danger"
        )

    return redirect(
        url_for("manager.employees")
    )


# ================= DELETE EMPLOYEE =================

@manager.route("/manager/delete-employee/<employee_id>")
def delete_employee(employee_id):

    if not manager_required():
        return redirect(url_for("auth.login"))

    success = Manager.delete_employee(employee_id)

    if success:

        flash(
            "Employee deleted successfully.",
            "success"
        )

    else:

        flash(
            "Unable to delete employee.",
            "danger"
        )

    return redirect(
        url_for("manager.employees")
    )


# ================= ANALYTICS =================

@manager.route("/manager/analytics")
def analytics():

    if not manager_required():
        return redirect(url_for("auth.login"))

    summary = get_dashboard_summary()

    recent_sales = Manager.get_recent_sales(100)

    month_labels, month_values = monthly_sales_chart()

    state_labels, state_values = state_sales_chart()

    fertilizer_labels, fertilizer_values = fertilizer_sales_chart()

    employee_labels, employee_values = employee_sales_chart()

    return render_template(

        "manager/analytics.html",

        summary=summary,

        recent_sales=recent_sales,

        month_labels=month_labels,
        month_values=month_values,

        state_labels=state_labels,
        state_values=state_values,

        fertilizer_labels=fertilizer_labels,
        fertilizer_values=fertilizer_values,

        employee_labels=employee_labels,
        employee_values=employee_values

    )

# ================= REPORTS =================

@manager.route("/manager/reports")
def reports():

    if not manager_required():
        return redirect(url_for("auth.login"))

    return render_template(

        "manager/reports.html",

        recent_sales=Manager.get_recent_sales(500)

    )


# ================= DOWNLOAD CSV =================

@manager.route("/manager/download-report")
def download_report():

    if not manager_required():
        return redirect(url_for("auth.login"))

    sales = Manager.get_recent_sales(10000)

    output = StringIO()

    writer = csv.writer(output)

    writer.writerow([
        "Date",
        "State",
        "District",
        "Fertilizer",
        "Quantity",
        "Amount"
    ])

    for row in sales:

        writer.writerow([

            row["sale_date"],

            row["state_name"],

            row["district_name"],

            row["fertilizer_name"],

            row["quantity"],

            row["total_amount"]

        ])

    output.seek(0)

    return Response(

        output.getvalue(),

        mimetype="text/csv",

        headers={

            "Content-Disposition":
            "attachment; filename=IFFCO_Sales_Report.csv"

        }

    )


# ================= SETTINGS =================

@manager.route("/manager/settings")
def settings():

    if not manager_required():
        return redirect(url_for("auth.login"))

    return render_template("manager/settings.html")