import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


MODEL_PATH = "models/forecast_model.pkl"


class ForecastModel:

    @staticmethod
    def train(df):

        features = [
            "Month",
            "Rainfall",
            "Temperature",
            "Price"
        ]

        target = "Demand"

        X = df[features]
        y = df[target]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        model = RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )

        model.fit(X_train, y_train)

        joblib.dump(model, MODEL_PATH)

        return model

    @staticmethod
    def load_model():
        return joblib.load(MODEL_PATH)

    @staticmethod
    def predict(month, rainfall, temperature, price):

        model = ForecastModel.load_model()

        data = pd.DataFrame([{
            "Month": month,
            "Rainfall": rainfall,
            "Temperature": temperature,
            "Price": price
        }])

        prediction = model.predict(data)

        return round(float(prediction[0]), 2)