from models.database import get_connection

import numpy as np

from sklearn.linear_model import LinearRegression


class Forecast:

    @staticmethod
    def predict(state_id, fertilizer_id):

        conn = get_connection()

        rows = conn.execute("""

            SELECT

                CAST(strftime('%m', sale_date) AS INTEGER) AS month,

                quantity

            FROM sales

            WHERE state_id=?

            AND fertilizer_id=?

            ORDER BY sale_date

        """,
        (
            state_id,
            fertilizer_id
        )).fetchall()

        conn.close()

        # Not enough data

        if len(rows) < 2:

            return {

                "prediction": 0,

                "confidence": 0,

                "demand": "No Data",

                "recommendation": "Not enough historical sales available.",

                "next_month": "--",

                "growth": 0,

                "trend": "No Trend",

                "risk": "Unknown",

                "recommended_stock": 0

            }

        months = []

        quantities = []

        for row in rows:

            months.append(row["month"])

            quantities.append(row["quantity"])

        X = np.array(months).reshape(-1,1)

        y = np.array(quantities)

        model = LinearRegression()

        model.fit(X, y)
        # ============================================
        # NEXT MONTH PREDICTION
        # ============================================

        next_month = months[-1] + 1

        if next_month > 12:

            next_month = 12

        prediction = model.predict([[next_month]])[0]

        prediction = max(0, round(prediction))

        # ============================================
        # CONFIDENCE
        # ============================================

        score = model.score(X, y)

        confidence = round(max(0, min(score * 100, 99)))

        # ============================================
        # GROWTH %
        # ============================================

        last_quantity = quantities[-1]

        if last_quantity == 0:

            growth = 0

        else:

            growth = round(

                ((prediction - last_quantity) / last_quantity) * 100,

                2

            )

        # ============================================
        # TREND
        # ============================================

        if growth > 10:

            trend = "Increasing"

        elif growth < -10:

            trend = "Decreasing"

        else:

            trend = "Stable"

        # ============================================
        # DEMAND LEVEL
        # ============================================

        if prediction >= 500:

            demand = "High"

        elif prediction >= 200:

            demand = "Medium"

        else:

            demand = "Low"

        # ============================================
        # RISK LEVEL
        # ============================================

        if confidence >= 85:

            risk = "Low"

        elif confidence >= 60:

            risk = "Medium"

        else:

            risk = "High"

        # ============================================
        # RECOMMENDED STOCK
        # ============================================

        recommended_stock = round(prediction * 1.15)
        # ============================================
        # AI RECOMMENDATION
        # ============================================

        if demand == "High":

            recommendation = (
                "Demand is expected to increase. "
                "Increase inventory and plan additional supply."
            )

        elif demand == "Medium":

            recommendation = (
                "Demand is stable. "
                "Maintain current inventory level."
            )

        else:

            recommendation = (
                "Demand is low. "
                "Reduce inventory and avoid overstocking."
            )

        # ============================================
        # MONTH NAME
        # ============================================

        month_names = [

            "Jan", "Feb", "Mar", "Apr",
            "May", "Jun", "Jul", "Aug",
            "Sep", "Oct", "Nov", "Dec"

        ]

        next_month_name = month_names[next_month - 1]

        # ============================================
        # AI BUSINESS INSIGHTS
        # ============================================

        if prediction >= 500:

            inventory = "Increase Inventory"

            procurement = "Place Purchase Order Immediately"

            distribution = "Increase Supply to Dealers"

            season = "Peak Season"

            alert = "Demand Spike Expected"

        elif prediction >= 200:

            inventory = "Maintain Current Inventory"

            procurement = "Normal Procurement"

            distribution = "Regular Distribution"

            season = "Normal Season"

            alert = "Demand Stable"

        else:

            inventory = "Reduce Inventory"

            procurement = "Delay Procurement"

            distribution = "Reduce Supply"

            season = "Off Season"

            alert = "Low Demand Alert"

        # ============================================
        # RETURN RESULT
        # ============================================

        return {

            "prediction": prediction,

            "confidence": confidence,

            "demand": demand,

            "recommendation": recommendation,

            "next_month": next_month_name,

            "growth": growth,

            "trend": trend,

            "risk": risk,

            "recommended_stock": recommended_stock,

            "history_labels": month_names[:len(months)],

            "history_values": quantities,
            
            "inventory": inventory,
            
            "procurement": procurement,
            
            "distribution": distribution,
            
            "season": season,
            
            "alert": alert,

        }
    
    # ============================================
# HISTORY
# ============================================

@staticmethod
def history():

    conn = get_connection()

    rows = conn.execute("""

        SELECT

            strftime('%m', sale_date) AS month,

            SUM(quantity) AS demand

        FROM sales

        GROUP BY month

        ORDER BY month

    """).fetchall()

    conn.close()

    month_names = [

        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec"

    ]

    labels = []

    values = []

    for row in rows:

        labels.append(

            month_names[int(row["month"]) - 1]

        )

        values.append(

            row["demand"]

        )

    return {

        "labels": labels,

        "values": values

    }