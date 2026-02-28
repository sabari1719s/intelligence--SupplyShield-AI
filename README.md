# 🛡️ SupplyShield AI

### Multi-Tier Supply Chain Fraud Detection System

## 📌 Overview

SupplyShield AI is an intelligent fraud detection system designed to identify financial fraud in multi-tier supply chain finance networks. The system analyzes supplier-buyer transactions across multiple tiers and detects suspicious patterns such as over-invoicing, duplicate financing, circular trading, and phantom suppliers.

Unlike traditional systems that analyze invoices individually, SupplyShield AI evaluates the entire transaction ecosystem using network-based analysis and machine learning.
## 🎯 Problem Statement

In supply chain finance, banks provide loans based on invoices between buyers and suppliers. Fraud can occur across multiple supplier tiers, making it difficult to detect using traditional invoice-level checks. This results in financial losses and increased risk exposure for financial institutions.

## 💡 Solution

SupplyShield AI solves this problem by:

* Building a supplier-buyer transaction network (graph model)
* Applying rule-based fraud detection
* Using Machine Learning (Isolation Forest) for anomaly detection
* Assigning risk scores to suppliers and transactions
* Flagging high-risk entities before loan approval
* Providing a real-time monitoring dashboard
## ⚙️ Technologies Used
* Python
* Pandas
* Scikit-learn
* NetworkX
* Streamlit (for dashboard)
* Matplotlib
## Features

* Over-invoicing detection
* Duplicate invoice detection
* Circular trading detection
* Anomaly detection using ML
* Risk scoring engine
* Fraud visualization dashboard

##  How to Run the Project

1. Install Python (3.9+ recommended)
2. Install required libraries:

```bash
pip install pandas scikit-learn networkx streamlit matplotlib

3. Run the fraud detection script:

```bash
python main.py

4. (Optional) Run dashboard:

```bash
streamlit run app.py

## 📈 Expected Impact

* Reduce financial fraud in supply chain finance
* Improve risk monitoring for banks
* Prevent cascading financial exposure
* Enable proactive fraud detection
## 👨‍💻 Developed For
Hackathon Project – Multi-Tier Supply Chain Fraud Detection

Tell me what you need next 🚀
