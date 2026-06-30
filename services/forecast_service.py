import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


def predict_next_revenue(revenue_trend):

    df = revenue_trend.copy()

    X = np.arange(len(df)).reshape(-1, 1)
    y = df["Revenue"].values

    model = LinearRegression()
    model.fit(X, y)

    next_day = np.array([[len(df)]])
    prediction = model.predict(next_day)[0]

    return round(prediction, 2)