# 🧠 Customer Segmentation Analysis
 
> A machine learning–powered Streamlit app that predicts which customer segment a person belongs to based on their demographic and behavioral data.

---
 
## 📌 Overview
 
This project applies **unsupervised machine learning** (K-Means Clustering) to segment customers into distinct groups based on their age, income, spending habits, purchase frequency, recency, and campaign engagement. The trained model is deployed as an interactive **Streamlit web app** for real-time predictions.
 
---

## 🎯 Customer Segments
 
The model identifies **6 distinct customer clusters**:
 
| Cluster | Label | Description |
|---------|-------|-------------|
| **0** | Low Income Low Spenders | Budget-conscious customers with lower engagement |
| **1** | Low Income Least Spenders | Minimal spending, least active segment |
| **2** | High Age Mid Spenders | Older customers with moderate spending patterns |
| **3** | Mid Age High Spenders | Active middle-aged customers with strong purchasing behavior |
| **4** | High Income Premium Buyers | High earners with premium spending habits |
| **5** | High Age High Spenders | Senior customers with high purchase volumes |
 
---
 
## 🖥️ Streamlit App (`app.py`)
 
The app takes the following **6 customer inputs** and predicts their segment in real time:
 
| Input | Range |
|-------|-------|
| Age | 18 – 100 |
| Annual Income | $0 – $200,000 |
| Total Spending | $0 – $5,000 |
| Number of Purchases | 0 – 50 |
| Recency (days since last visit) | 0 – 99 |
| Total Campaigns Accepted | 0 – 4 |
 
---

## 🚀 Getting Started
 
### Prerequisites
 
- Python 3.x
- pip
### Installation
 
```bash
# 1. Clone the repository
git clone https://github.com/RaviNamdeoo/Customer_Segmentation_Analysis.git
cd Customer_Segmentation_Analysis
 
# 2. Install dependencies
pip install -r requirements.txt
 
# 3. Run the Streamlit app
streamlit run app.py
```
 
The app will open at `http://localhost:8501` in your browser.
 
---
 
## 📦 Dependencies
 
```
pandas
numpy
scikit-learn==1.8.0
matplotlib
seaborn
streamlit
```
 
---
 
## 🌐 Live Demo
 
Try the deployed app here: **[customer-segmentation-analysis-ravi.streamlit.app](https://customer-segmentation-analysis-ravi.streamlit.app/)**
 
---
 
## 🏷️ Topics
 
`data-science` · `machine-learning` · `data-analysis` · `k-means-clustering` · `streamlit` · `customer-segmentation`
 
---
 
## 👤 Author
 
**Ravi Namdeo**
- GitHub: [@RaviNamdeoo](https://github.com/RaviNamdeoo)
