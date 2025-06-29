# Dynamic Pricing Optimization for Hosts
📍Problem:
Hosts often underprice or overprice their listings due to lack of insight.

💡Solution:
- Build a price recommendation engine that:
- Suggests optimal nightly prices
- Adapts to seasonality and competition in the area
- Accounts for rating, availability, and room type

🔧 Use calendar.csv + listings.csv for building this.

Steps:
- Make folder structure
- Download the data
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)

Structure:
'''
AirbnbDynamicPricing/
├── data/
│   ├── listings.csv
│   ├── calendar.csv
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_modeling.ipynb
├── src/
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── predict_price.py
├── app/
│   ├── streamlit_app.py
├── models/
│   ├── price_model.pkl
├── requirements.txt
├── README.md
'''
