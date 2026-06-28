from flask import Blueprint, render_template, request, redirect, session, flash, url_for

auth = Blueprint("auth", __name__)

USERS = {

    "MGR001": {
        "name": "Manager",
        "password": "admin123",
        "role": "manager"
    },

    "EMP001": {
        "name": "Avinash Bhardwaj",
        "password": "emp123",
        "role": "employee"
    },

    "EMP002": {
        "name": "Aman Rajput",
        "password": "emp123",
        "role": "employee"
    },

    "EMP003": {
        "name": "Adarsh Bhardwaj",
        "password": "emp123",
        "role": "employee"
    },

    "EMP004": {
        "name": "Nanak Pandey",
        "password": "emp123",
        "role": "employee"
    },

    "EMP005": {
        "name": "Amul Singh",
        "password": "emp123",
        "role": "employee"
    },

    "EMP006": {
        "name": "Rahul Verma",
        "password": "emp123",
        "role": "employee"
    }

}


@auth.route("/login", methods=["GET", "POST"])
def login():

    if session.get("user_role") == "manager":
        return redirect(url_for("manager.dashboard"))

    if session.get("user_role") == "employee":
        return redirect(url_for("employee.dashboard"))

    if request.method == "POST":

        employee_id = request.form.get("employee_id", "").strip().upper()
        password = request.form.get("password", "").strip()

        user = USERS.get(employee_id)

        if user and user["password"] == password:

            session.clear()

            session["user_id"] = employee_id
            session["employee_id"] = employee_id
            session["employee_name"] = user["name"]
            session["user_role"] = user["role"]

            if user["role"] == "manager":
                return redirect(url_for("manager.dashboard"))

            return redirect(url_for("employee.dashboard"))

        flash("Invalid Employee ID or Password", "danger")

    return render_template("login.html")


@auth.route("/logout")
def logout():

    session.clear()

    flash("Logged out successfully.", "success")

    return redirect(url_for("auth.login"))