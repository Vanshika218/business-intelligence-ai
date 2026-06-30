import pandas as pd


def analyze_inventory(path):

    df = pd.read_csv(path)

    low_stock = df[df["Stock"] < 50]

    return {

        "low_stock_products": list(low_stock["Product"]),

        "inventory_df": df

    }