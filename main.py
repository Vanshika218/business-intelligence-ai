from agents.sales_agent import analyze_sales
from agents.inventory_agent import analyze_inventory
from agents.review_agent import analyze_reviews
from agents.manager_agent import generate_business_report


sales_result = analyze_sales("data/sales.csv")
inventory_result = analyze_inventory("data/inventory.csv")
review_result = analyze_reviews("data/reviews.csv")

report = generate_business_report(
    sales_result,
    inventory_result,
    review_result
)

print(report)