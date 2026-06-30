import pandas as pd


def analyze_sales(path):

    df = pd.read_csv(path)

    total_revenue = df["Revenue"].sum()

    total_units = df["UnitsSold"].sum()

    top_product = (
        df.groupby("Product")["Revenue"]
        .sum()
        .idxmax()
    )

    revenue_by_product = (
        df.groupby("Product")["Revenue"]
        .sum()
        .reset_index()
    )

    revenue_trend = (
        df.groupby("Date")["Revenue"]
        .sum()
        .reset_index()
    )

    return {

        "total_revenue": total_revenue,

        "total_units": total_units,

        "top_product": top_product,

        "revenue_by_product": revenue_by_product,

        "revenue_trend": revenue_trend
    }