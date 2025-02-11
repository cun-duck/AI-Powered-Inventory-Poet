import pandas as pd

class InventoryCleaner:
    def __init__(self, filepath):
        self.df = pd.read_excel(filepath)
        
    def clean_data(self):
        # Handle missing values
        self.df['stock_level'] = self.df['stock_level'].fillna(0)
        
        # Convert date formats
        self.df['last_updated'] = pd.to_datetime(self.df['last_updated'])
        
        # Categorize urgency
        self.df['status'] = self.df.apply(lambda row: 
            'Critical' if row['stock_level'] < row['min_threshold'] 
            else 'Adequate', axis=1)
        
        return self.df
