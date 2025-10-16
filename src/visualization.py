import matplotlib.pyplot as plt

def plot_sales_trend(df):
    # Plot total weekly sales trend over time
    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Weekly_Sales'], color='royalblue', linewidth=1)
    plt.title("Walmart Weekly Sales Over Time")
    plt.xlabel("Date")
    plt.ylabel("Weekly Sales ($)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_correlation(df):
    # Scatter plots
    plt.figure(figsize=(14,5))
    plt.subplot(1,2,1)
    plt.title("Temperature vs Weekly Sales")
    plt.xlabel("Temperature (F)")
    plt.ylabel("Weekly Sales ($)")

    plt.subplot(1,2,2)
    plt.scatter(df['Fuel_Price'], df['Weekly_Sales'], alpha=0.5, color='green')
    plt.title("Fuel Price vs Weekly Sales")
    plt.xlabel("Fuel Price ($)")
    plt.ylabel("Weekly Sales ($)")

    plt.tight_layout()
    plt.show()