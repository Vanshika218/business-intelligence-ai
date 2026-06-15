import pandas as pd


def analyze_inventory(path):

    df = pd.read_csv(path)

    low_stock_products = []

    forecast = []

    for _, row in df.iterrows():

        if row["Stock"] < 50:

            low_stock_products.append(
                row["Product"]
            )

            forecast.append(
                f"{row['Product']} may run out soon"
            )

    return {
        "low_stock_products": low_stock_products,
        "forecast": forecast
    }