import os
import pandas as pd
from config import Config


class DataPreprocessor:
    """
    Handles data preprocessing for the
    IFFCO Fertilizer Demand Forecasting Project.
    """

    def __init__(self):
        self.processed_folder = Config.PROCESSED_DATA_FOLDER

    def clean_column_names(self, df):
        """
        Clean column names.
        """
        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )
        return df

    def remove_duplicates(self, df):
        """
        Remove duplicate records.
        """
        return df.drop_duplicates()

    def handle_missing_values(self, df):
        """
        Fill missing values.
        """
        return df.fillna(method="ffill")

    def convert_date_column(self, df, column_name="date"):
        """
        Convert date column into datetime.
        """
        if column_name in df.columns:
            df[column_name] = pd.to_datetime(df[column_name])
        return df

    def sort_data(self, df, column_name="date"):
        """
        Sort dataset by date.
        """
        if column_name in df.columns:
            df = df.sort_values(by=column_name)
        return df

    def save_processed_data(self, df, filename="cleaned_data.csv"):
        """
        Save cleaned dataset.
        """
        filepath = os.path.join(self.processed_folder, filename)
        df.to_csv(filepath, index=False)
        return filepath

    def preprocess(self, df):
        """
        Complete preprocessing pipeline.
        """
        df = self.clean_column_names(df)
        df = self.remove_duplicates(df)
        df = self.handle_missing_values(df)
        df = self.convert_date_column(df)
        df = self.sort_data(df)

        self.save_processed_data(df)

        return df