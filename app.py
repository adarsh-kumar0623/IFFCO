from flask import Flask, render_template, redirect, url_for, session

from config import Config

from routes.auth import auth
from routes.manager import manager
from routes.employee import employee
from routes.analytics import analytics
from routes.forecast import forecast

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(auth)
app.register_blueprint(manager)
app.register_blueprint(employee)
app.register_blueprint(analytics)
app.register_blueprint(forecast)


@app.route("/")
def index():

    if "user_role" not in session:
        return redirect(url_for("auth.login"))

    if session["user_role"] == "manager":
        return redirect(url_for("manager.dashboard"))

    return redirect(url_for("employee.dashboard"))


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)