import numpy as np
import pandas as pd
from src.data_cleaning import load_data, clean_data
from src.visualization import plot_sales_trend, plot_correlation

def main():
    df = load_data("data/Walmart_Sales.csv")
    df = clean_data(df)

    # Converting Weekly Sales to numpy array
    sales = df['Weekly_Sales'].to_numpy()

    print("Walmart Sales Analysis\n")
    print(f"Total Entries: {len(df)}")
    print(f"Average Weekly Sales: {np.mean(sales):.2f}")
    print(f"Maximum Weekly Sales: {np.max(sales):.2f}")
    print(f"Minimum Weekly Sales: {np.min(sales):.2f}")

    # Correlation analysis
    temp_corr = np.corrcoef(df['Weekly_Sales'], df['Temperature'])[0,1]
    fuel_corr = np.corrcoef(df['Weekly_Sales'], df['Fuel_Price'])[0, 1]
    cpi_corr = np.corrcoef(df['Weekly_Sales'], df['CPI'])[0,1]

    print("Correlation with Weekly Sales:")
    print(f"Temperature: {temp_corr:.3f}")
    print(f"Fuel Price: {fuel_corr:.3f}")
    print(f"CPI: {cpi_corr:.3f}")

    # Visualizations
    plot_sales_trend(df)
    plot_correlation(df)

if __name__=="__main__":
    main()