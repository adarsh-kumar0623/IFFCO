from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    url_for,
    request
)

from utils.master_data import (
    get_states,
    get_fertilizers
)

from models.forecast import Forecast

forecast = Blueprint("forecast", __name__)


def manager_required():

    return session.get("user_role") == "manager"


# =====================================================
# FORECAST HOME
# =====================================================

@forecast.route("/forecast")
def forecast_dashboard():

    if not manager_required():

        return redirect(url_for("auth.login"))

    return render_template(

        "forecast.html",

        states=get_states(),

        fertilizers=get_fertilizers(),

        predicted_demand=0,

        confidence="--",

        demand="--",

        recommendation="Select State and Fertilizer to generate AI prediction.",

        next_month="--",

        growth=0,

        trend="--",

        risk="--",

        recommended_stock=0,

        history_labels=[],

        history_values=[],

        inventory="--",

        procurement="--",

        distribution="--",

        season="--",

        alert="--"

    )


# =====================================================
# PREDICT
# =====================================================

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

    growth = 0

    trend = "--"

    risk = "--"

    recommended_stock = 0

    history_labels = []

    history_values = []

    inventory = "--"

    procurement = "--"

    distribution = "--"

    season = "--"

    alert = "--"

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

        growth = result["growth"]

        trend = result["trend"]

        risk = result["risk"]

        recommended_stock = result["recommended_stock"]

        history_labels = result["history_labels"]

        history_values = result["history_values"]

        inventory = result["inventory"]

        procurement = result["procurement"]

        distribution = result["distribution"]

        season = result["season"]

        alert = result["alert"]

    return render_template(

        "forecast.html",

        states=states,

        fertilizers=fertilizers,

        predicted_demand=prediction,

        confidence=confidence,

        demand=demand,

        recommendation=recommendation,

        next_month=next_month,

        growth=growth,

        trend=trend,

        risk=risk,

        recommended_stock=recommended_stock,

        history_labels=history_labels,

        history_values=history_values,

        inventory=inventory,

        procurement=procurement,

        distribution=distribution,

        season=season,

        alert=alert

    )


# =====================================================
# HISTORY API
# =====================================================

@forecast.route("/forecast/history")
def history():

    if not manager_required():

        return redirect(url_for("auth.login"))

    rows = Forecast.history()

    return {

        "history": [

            dict(row)

            for row in rows

        ]

    }