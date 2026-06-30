import plotly.express as px


def revenue_chart(df):
    fig = px.bar(
        df,
        x="Product",
        y="Revenue",
        title="Revenue by Product",
        text="Revenue",
        color="Revenue"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Product",
        yaxis_title="Revenue (₹)"
    )

    return fig


def revenue_trend_chart(df):
    fig = px.line(
        df,
        x="Date",
        y="Revenue",
        title="Revenue Trend",
        markers=True
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Date",
        yaxis_title="Revenue (₹)"
    )

    return fig


def inventory_chart(df):
    fig = px.bar(
        df,
        x="Product",
        y="Stock",
        title="Inventory Status",
        text="Stock",
        color="Stock"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Product",
        yaxis_title="Stock"
    )

    return fig