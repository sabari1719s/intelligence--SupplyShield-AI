from sklearn.ensemble import IsolationForest

def run_ml_model(df):

    features = df[['amount_deviation','supplier_centrality','invoice_frequency']]

    model = IsolationForest(contamination=0.25, random_state=42)
    df['ml_prediction'] = model.fit_predict(features)

    df['ml_flag'] = df['ml_prediction'].apply(lambda x: 1 if x == -1 else 0)

    return df
