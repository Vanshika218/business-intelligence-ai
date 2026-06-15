import pandas as pd


def analyze_reviews(path):

    df = pd.read_csv(path)

    complaints = []

    for review in df["Review"]:

        review = review.lower()

        if "late" in review:
            complaints.append(
                "Delivery Delay"
            )

        if "slow" in review:
            complaints.append(
                "Shipping Delay"
            )

    return {
        "total_reviews": len(df),
        "complaints": list(set(complaints))
    }