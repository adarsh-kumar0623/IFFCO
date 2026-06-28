import pandas as pd
import os


class DataLoader:

    @staticmethod
    def load_csv(file_path):
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return None

    @staticmethod
    def load_excel(file_path):
        try:
            return pd.read_excel(file_path)
        except Exception as e:
            print(f"Error loading Excel: {e}")
            return None

    @staticmethod
    def save_csv(dataframe, filename):
        try:
            save_path = os.path.join("static", "downloads", filename)
            dataframe.to_csv(save_path, index=False)
            return save_path
        except Exception as e:
            print(f"Error saving CSV: {e}")
            return None

    @staticmethod
    def clean_data(df):
        if df is None:
            return None

        df = df.drop_duplicates()
        df = df.dropna(how="all")
        df.columns = [col.strip() for col in df.columns]

        return df

    @staticmethod
    def preview(df, rows=5):
        if df is None:
            return None

        return df.head(rows)