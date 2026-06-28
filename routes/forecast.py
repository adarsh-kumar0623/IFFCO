from flask import Blueprint, render_template, session, redirect, url_for, request

from utils.master_data import get_states, get_fertilizers
from models.forecast import Forecast

forecast = Blueprint("forecast", __name__)


def manager_required():
    return session.get("user_role") == "manager"


@forecast.route("/forecast")
def forecast_dashboard():

    if not manager_required():
        return redirect(url_for("auth.login"))

    states = get_states()
    fertilizers = get_fertilizers()

    return render_template(
        "forecast.html",
        states=states,
        fertilizers=fertilizers,
        predicted_demand=0,
        confidence="--"
    )


@forecast.route("/forecast/predict", methods=["GET"])
def predict():

    if not manager_required():
        return redirect(url_for("auth.login"))

    states = get_states()
    fertilizers = get_fertilizers()

    state_id = request.args.get("state")
    fertilizer_id = request.args.get("fertilizer")

    prediction = 0
    confidence = "--"
    demand = "--"
    recommendation = "--"
    next_month = "--"

    if state_id and fertilizer_id:
        result = Forecast.predict(
            int(state_id),
            int(fertilizer_id)
        )
        prediction = result["prediction"]
        confidence = f'{result["confidence"]}%'
        demand = result["demand"]
        recommendation = result["recommendation"]
        next_month = result["next_month"]

    return render_template(
        "forecast.html",
        states=states,
        fertilizers=fertilizers,
        predicted_demand=prediction,
        confidence=confidence,
        demand=demand,
        recommendation=recommendation,
        next_month=next_month
    )


@forecast.route("/forecast/history")
def history():

    if not manager_required():
        return redirect(url_for("auth.login"))

    history = Forecast.history()

    return {
        "history": [
            dict(row) for row in history
        ]
    }