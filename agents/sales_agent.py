import pandas as pd


def analyze_sales(path):

    df = pd.read_csv(path)

    total_revenue = df["Revenue"].sum()

    total_units = df["UnitsSold"].sum()

    revenue_by_product = (
        df.groupby("Product")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    top_product = revenue_by_product.index[0]

    top_product_revenue = revenue_by_product.iloc[0]

    revenue_share = round(
        (top_product_revenue / total_revenue) * 100,
        2
    )

    return {
        "total_revenue": total_revenue,
        "total_units": total_units,
        "top_product": top_product,
        "revenue_share": revenue_share
    }