import pandas as pd

class DataValidator:
    @staticmethod
    def validate_structure(df):
        required_columns = ['item_id', 'item_name', 'category', 
                           'stock_level', 'min_threshold', 'last_updated']
        if not all(col in df.columns for col in required_columns):
            raise ValueError("Missing required columns in Excel file")
            
    @staticmethod
    def validate_data_types(df):
        if not pd.api.types.is_datetime64_any_dtype(df['last_updated']):
            raise TypeError("last_updated must be datetime format")
