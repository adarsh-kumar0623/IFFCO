import pandas as pd
import matplotlib.pyplot as plt
import os


class ChartGenerator:

    @staticmethod
    def monthly_sales_chart(df):

        monthly = (
            df.groupby("Month")["Total_Amount"]
            .sum()
            .reset_index()
        )

        plt.figure(figsize=(10, 5))
        plt.plot(
            monthly["Month"],
            monthly["Total_Amount"],
            marker="o",
            linewidth=2
        )

        plt.title("Monthly Fertilizer Sales")
        plt.xlabel("Month")
        plt.ylabel("Total Sales")
        plt.grid(True)

        os.makedirs("static/images", exist_ok=True)

        path = "static/images/monthly_sales.png"

        plt.savefig(path, dpi=300, bbox_inches="tight")
        plt.close()

        return path

    @staticmethod
    def state_sales_chart(df):

        state = (
            df.groupby("State")["Total_Amount"]
            .sum()
            .sort_values(ascending=False)
        )

        plt.figure(figsize=(10, 5))

        state.plot(kind="bar")

        plt.title("State Wise Sales")
        plt.xlabel("State")
        plt.ylabel("Total Sales")

        plt.tight_layout()

        os.makedirs("static/images", exist_ok=True)

        path = "static/images/state_sales.png"

        plt.savefig(path, dpi=300)
        plt.close()

        return path

    @staticmethod
    def fertilizer_chart(df):

        fertilizer = (
            df.groupby("Fertilizer")["Quantity"]
            .sum()
        )

        plt.figure(figsize=(8, 8))

        fertilizer.plot(
            kind="pie",
            autopct="%1.1f%%"
        )

        plt.ylabel("")

        os.makedirs("static/images", exist_ok=True)

        path = "static/images/fertilizer_distribution.png"

        plt.savefig(path, dpi=300)
        plt.close()

        return path