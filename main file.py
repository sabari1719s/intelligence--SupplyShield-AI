import streamlit as st
import matplotlib.pyplot as plt
from src.preprocessing import preprocess_data
from src.graph_engine import build_graph, calculate_centrality, detect_cycles
from src.fraud_rules import apply_rules
from src.ml_model import run_ml_model
from src.risk_engine import calculate_risk

st.set_page_config(page_title="SupplyShield AI", layout="wide")
st.title("🚨 SupplyShield AI - Multi-Tier Fraud Detection")

# Load & Process Data
df = preprocess_data("data/invoice_data.csv")

# Apply Fraud Rules
df = apply_rules(df)

# Graph Analysis
G = build_graph(df)
df = calculate_centrality(G, df)
cycles = detect_cycles(G)

# ML Model
df = run_ml_model(df)

# Risk Engine
df = calculate_risk(df)

# Display Results
st.subheader("📊 Invoice Analysis")
st.dataframe(df)

# High Risk
st.subheader("🔥 High Risk Invoices")
st.dataframe(df[df['risk_level']=="High"])

# Show Graph
st.subheader("🌐 Supply Chain Network Graph")
plt.figure()
pos = build_graph(df)
import networkx as nx
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
st.pyplot(plt)

# Show Cycles
st.subheader("🔁 Circular Trading Detection")
if cycles:
    st.write(cycles)
else:
    st.write("No circular trading detected.")

st.success("System Successfully Detected Multi-Tier Fraud 🚀")
