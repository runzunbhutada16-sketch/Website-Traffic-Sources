import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os
from tabulate import tabulate
import warnings
warnings.filterwarnings('ignore')

class TrafficAnalyzer:
    """
    A class for analyzing and visualizing website traffic data.
    Follows OOP principles for professional web analytics.
    """

    def __init__(self, data_path='website_traffic.csv'):
        """
        Initialize the analyzer with data path.
        """
        self.data_path = data_path
        self.df = None
        self.load_data()
        self.clean_data()
        self.reports_dir = 'reports'
        os.makedirs(self.reports_dir, exist_ok=True)

    def load_data(self):
        """Load data from CSV file."""
        try:
            self.df = pd.read_csv(self.data_path)
            print(f" Loaded {len(self.df)} records from {self.data_path}")
        except FileNotFoundError:
            print(" Data file not found. Please check the path.")
            raise
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            raise

    def clean_data(self):
        """Clean and preprocess the dataset."""
        print("🧹 Cleaning data...")

        # Handle missing values
        initial_len = len(self.df)
        self.df = self.df.dropna(subset=['Date', 'Source', 'Visits'])
        print(f"   Removed {initial_len - len(self.df)} rows with missing critical values.")

        # Handle duplicates
        dupes = self.df.duplicated().sum()
        self.df = self.df.drop_duplicates()
        print(f"   Removed {dupes} duplicate records.")

        # Convert Date to datetime
        self.df['Date'] = pd.to_datetime(self.df['Date'], errors='coerce')
        invalid_dates = self.df['Date'].isna().sum()
        self.df = self.df.dropna(subset=['Date'])
        print(f"   Removed {invalid_dates} rows with invalid dates.")

        # Standardize Source names
        source_map = {
            'organic search': 'Organic Search',
            'paid search': 'Paid Search',
            'social media': 'Social Media',
            'direct': 'Direct',
            'email': 'Email',
            'referral': 'Referral'
        }
        self.df['Source'] = self.df['Source'].str.strip().str.title()
        self.df['Source'] = self.df['Source'].replace(source_map)

        # Ensure numeric columns
        numeric_cols = ['Visits', 'Conversions', 'BounceRate', 'SessionDuration']
        for col in numeric_cols:
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce')

        self.df = self.df.dropna(subset=numeric_cols)

        # Add derived columns
        self.df['Year'] = self.df['Date'].dt.year
        self.df['Month'] = self.df['Date'].dt.month
        self.df['Quarter'] = self.df['Date'].dt.quarter
        self.df['ConversionRate'] = (self.df['Conversions'] / self.df['Visits']) * 100

        print(f" Data cleaned. Final dataset: {len(self.df)} records.")

    def get_summary(self):
        """Get dataset summary."""
        summary = {
            'Total Records': len(self.df),
            'Date Range': f"{self.df['Date'].min().date()} to {self.df['Date'].max().date()}",
            'Total Visits': self.df['Visits'].sum(),
            'Total Conversions': self.df['Conversions'].sum(),
            'Avg Bounce Rate': round(self.df['BounceRate'].mean(), 3),
            'Avg Session Duration': round(self.df['SessionDuration'].mean(), 1),
            'Unique Sources': self.df['Source'].nunique(),
            'Unique Countries': self.df['Country'].nunique()
        }
        return summary

    # ... (rest of the methods as implemented: analyze_traffic_trends, traffic_source_performance, etc.)

    def display_menu(self):
        """Interactive terminal dashboard."""
        # (Full menu implementation as in the file)

def main():
    """Main function to run the application."""
    print(" Starting Website Traffic Sources Analysis...")
    try:
        analyzer = TrafficAnalyzer()
        analyzer.display_menu()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
