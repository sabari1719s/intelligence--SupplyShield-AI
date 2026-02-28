def calculate_risk(df):

    df['risk_score'] = (
        abs(df['amount_deviation']) * 0.25 +
        df['supplier_centrality'] * 100 * 0.25 +
        df['invoice_frequency'] * 0.2 +
        df['over_invoice_flag'].astype(int) * 15 +
        df['ml_flag'] * 15
    )

    df['risk_level'] = df['risk_score'].apply(
        lambda x: "High" if x > 75 else ("Medium" if x > 40 else "Low")
    )

    return df
