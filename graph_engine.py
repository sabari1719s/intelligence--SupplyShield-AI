import networkx as nx

def build_graph(df):
    G = nx.DiGraph()

    for _, row in df.iterrows():
        G.add_edge(row['supplier_id'], row['buyer_id'], amount=row['amount'])

    return G

def calculate_centrality(G, df):
    centrality = nx.degree_centrality(G)
    df['supplier_centrality'] = df['supplier_id'].map(centrality)
    df['supplier_centrality'] = df['supplier_centrality'].fillna(0)
    return df

def detect_cycles(G):
    try:
        cycles = list(nx.simple_cycles(G))
        return cycles
    except:
        return []
