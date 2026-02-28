def apply_rules(df):

    # Rule 1: Over Invoicing (40% above average)
    avg_amount = df['amount'].mean()
    df['over_invoice_flag'] = df['amount'] > (avg_amount * 1.4)

    # Rule 2: Duplicate Supplier-Buyer invoices
    df['duplicate_flag'] = df.duplicated(subset=['supplier_id','buyer_id','amount'], keep=False)

    return df
