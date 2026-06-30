from services.llm_service import generate_response


def generate_business_report(sales, inventory, reviews):

    prompt = f"""
You are a Senior Business Intelligence Consultant.

Analyze the following business data and generate a professional business report.

Sales Summary:
- Total Revenue: ₹{sales['total_revenue']}
- Total Units Sold: {sales['total_units']}
- Top Product: {sales['top_product']}

Inventory Summary:
- Low Stock Products: {', '.join(inventory['low_stock_products'])}

Customer Reviews:
- Total Reviews: {reviews['total_reviews']}
- Positive Reviews: {reviews['positive_reviews']}
- Negative Reviews: {reviews['negative_reviews']}
- Positive Percentage: {reviews['positive_percentage']}%

Generate a clean professional business report.

Rules:

- Do NOT use Markdown.
- Do NOT use ## headings.
- Do NOT use **bold**.
- Do NOT use --- separators.
- Use CAPITAL LETTER headings.
- Leave one blank line between sections.
- Use numbered recommendations.
- Keep the report concise and executive-friendly.
- Output plain text only.

Keep it professional and concise.
"""

    return generate_response(prompt)