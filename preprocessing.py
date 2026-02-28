import pandas as pd

def preprocess_data(filepath):
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'])

    # Amount deviation
    avg_amount = df['amount'].mean()
    df['amount_deviation'] = df['amount'] - avg_amount

    # Invoice frequency
    df['invoice_frequency'] = df.groupby('supplier_id')['invoice_id'].transform('count')

    return df
