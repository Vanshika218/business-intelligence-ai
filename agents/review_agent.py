import pandas as pd


def analyze_reviews(path):

    df = pd.read_csv(path)

    positive_words = [
        "excellent",
        "good",
        "great",
        "soft",
        "love",
        "quality"
    ]

    negative_words = [
        "late",
        "bad",
        "poor",
        "delay",
        "slow"
    ]

    positive = 0
    negative = 0

    for review in df["Review"]:

        review = review.lower()

        if any(word in review for word in positive_words):
            positive += 1

        if any(word in review for word in negative_words):
            negative += 1

    total = len(df)

    positive_percentage = round((positive / total) * 100, 2)

    return {
        "total_reviews": total,
        "positive_reviews": positive,
        "negative_reviews": negative,
        "positive_percentage": positive_percentage
    }