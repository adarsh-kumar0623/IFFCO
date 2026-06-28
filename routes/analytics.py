from flask import Blueprint, render_template, session, redirect, url_for

from models.dashboard import get_dashboard_summary
from models.manager import Manager

analytics = Blueprint("analytics", __name__)


def manager_required():

    return session.get("user_role") == "manager"


@analytics.route("/analytics")
def analytics_dashboard():

    if not manager_required():
        return redirect(url_for("auth.login"))

    summary = get_dashboard_summary()

    recent_sales = Manager.get_recent_sales(100)

    return render_template(
        "manager/analytics.html",
        summary=summary,
        recent_sales=recent_sales
    )


@analytics.route("/analytics/sales")
def sales_analysis():

    return analytics_dashboard()


@analytics.route("/analytics/state")
def state_analysis():

    return analytics_dashboard()


@analytics.route("/analytics/season")
def season_analysis():

    return analytics_dashboard()