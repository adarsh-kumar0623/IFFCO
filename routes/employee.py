from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    url_for,
    request,
    flash
)

from models.employee import Employee

from utils.master_data import (
    get_states,
    get_districts,
    get_fertilizers
)

employee = Blueprint("employee", __name__)


# =====================================================
# AUTH
# =====================================================

def employee_required():

    return session.get("user_role") == "employee"


# =====================================================
# DASHBOARD
# =====================================================

@employee.route("/employee/dashboard")
def dashboard():

    if not employee_required():

        return redirect(url_for("auth.login"))

    employee_id = session["employee_id"]

    summary = Employee.get_dashboard(employee_id)

    history = Employee.get_sales_history(employee_id)[:10]

    return render_template(

        "employee/dashboard.html",

        summary=summary,

        history=history,

        employee_name=session.get("employee_name"),

        employee_id=employee_id,

        designation="Sales Executive",

        branch="Bareilly Branch"

    )


# =====================================================
# SALES ENTRY
# =====================================================

@employee.route("/employee/sales-entry", methods=["GET", "POST"])
def sales_entry():

    if not employee_required():

        return redirect(url_for("auth.login"))

    if request.method == "POST":

        Employee.save_sale(

            session["employee_id"],

            request.form["state"],

            request.form["district"],

            request.form["fertilizer"],

            request.form["quantity"]

        )

        flash(

            "Sales Entry Saved Successfully.",

            "success"

        )

        return redirect(

            url_for("employee.history")

        )

    return render_template(

        "employee/sales_entry.html",

        states=get_states(),

        fertilizers=get_fertilizers()

    )


# =====================================================
# SALES HISTORY
# =====================================================

@employee.route("/employee/history")
def history():

    if not employee_required():

        return redirect(url_for("auth.login"))

    history = Employee.get_sales_history(

        session["employee_id"]

    )

    return render_template(

        "employee/history.html",

        history=history

    )


# =====================================================
# DELETE SALE
# =====================================================

@employee.route("/employee/delete-sale/<int:sale_id>")
def delete_sale(sale_id):

    if not employee_required():

        return redirect(url_for("auth.login"))

    Employee.delete_sale(sale_id)

    flash(

        "Sales Record Deleted Successfully.",

        "success"

    )

    return redirect(

        url_for("employee.history")

    )


# =====================================================
# PROFILE
# =====================================================

@employee.route("/employee/profile")
def profile():

    if not employee_required():

        return redirect(url_for("auth.login"))

    return render_template(

        "employee/profile.html"

    )


# =====================================================
# DISTRICT AJAX
# =====================================================

@employee.route("/employee/get-districts/<int:state_id>")
def get_state_districts(state_id):

    districts = get_districts(state_id)

    return [

        dict(row)

        for row in districts

    ]