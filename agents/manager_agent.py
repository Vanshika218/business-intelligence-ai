def generate_business_report(
    sales,
    inventory,
    reviews
):

    report = f"""

BUSINESS INTELLIGENCE REPORT

Revenue:
₹{sales['total_revenue']}

Best Selling Product:
{sales['top_product']}

Revenue Contribution:
{sales['revenue_share']}%

Low Stock Products:
{', '.join(inventory['low_stock_products'])}

Customer Issues:
{', '.join(reviews['complaints'])}

RECOMMENDATIONS

1. Increase stock for low inventory products.

2. Promote {sales['top_product']}
through digital marketing.

3. Improve delivery operations.

4. Focus on high-margin textile products.

"""

    return report