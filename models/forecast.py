from models.database import get_connection

import numpy as np

from sklearn.linear_model import LinearRegression


class Forecast:

    @staticmethod
    def predict(state_id, fertilizer_id):

        conn = get_connection()

        rows = conn.execute("""

            SELECT

                CAST(strftime('%m',sale_date) AS INTEGER) month,

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
                "recommendation": "Not enough sales data available.",
                "next_month": "--"
            }
        X = np.array(
            [row["month"] for row in rows]
        ).reshape(-1,1)

        y = np.array(
            [row["quantity"] for row in rows]
        )

        model = LinearRegression()

        model.fit(X,y)

        next_month = int(max(X)[0]) + 1

        if next_month > 12:
            next_month = 12

        prediction = model.predict([[next_month]])[0]

        prediction = max(0, round(prediction))

        score = model.score(X,y)

        confidence = max(0, round(score*100))

        if prediction >= 500:
            demand = "High"
            recommendation = "Increase stock immediately. High demand is expected."
        elif prediction >= 200:
            demand = "Medium"
            recommendation = "Maintain normal inventory level."
        else:
            demand = "Low"
            recommendation = "Reduce inventory and avoid overstocking."
        return {
            "prediction": prediction,
            "confidence": confidence,
            "demand": demand,
            "recommendation": recommendation,
            "next_month": next_month
        }


    @staticmethod
    def history():

        conn = get_connection()

        rows = conn.execute("""

            SELECT

                sale_date,

                SUM(quantity) demand

            FROM sales

            GROUP BY sale_date

            ORDER BY sale_date

        """).fetchall()

        conn.close()

        return rows