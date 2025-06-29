import pandas as pd
import numpy as np
import os

# Paths
LISTINGS_PATH = "/Users/fahimulkabir/Github/Airbnb Pricing Optimization/data/raw/New York/New York City/listings.csv"
CALENDAR_PATH = "/Users/fahimulkabir/Github/Airbnb Pricing Optimization/data/raw/New York/New York City/calendar.csv"
SAVE_PATH = "/Users/fahimulkabir/Github/Airbnb Pricing Optimization/data/processed/New York/New York City"

os.makedirs(SAVE_PATH, exist_ok=True)

# === 1. Load listings.csv ===
listings = pd.read_csv(LISTINGS_PATH, low_memory=False)

# Keep only relevant columns
listings = listings[[
    'id', 'neighbourhood_cleansed', 'latitude', 'longitude',
    'room_type', 'minimum_nights', 'number_of_reviews',
    'review_scores_rating', 'availability_365'
]]

# Rename for clarity
listings.rename(columns={'id': 'listing_id'}, inplace=True)

# Impute missing values
listings['review_scores_rating'] = listings['review_scores_rating'].fillna(listings['review_scores_rating'].median())
listings['number_of_reviews'] = listings['number_of_reviews'].fillna(0)

# Encode categorical feature
listings = pd.get_dummies(listings, columns=['room_type', 'neighbourhood_cleansed'], drop_first=True)

# === 2. Load calendar.csv ===
calendar = pd.read_csv(CALENDAR_PATH)

# Convert date to datetime
calendar['date'] = pd.to_datetime(calendar['date'])

# Clean price column
calendar['price'] = (
    calendar['price']
    .astype(str)
    .str.replace(r'[\$,]', '', regex=True)
    .astype(float)
)

# Drop rows with price 0 or NA
calendar = calendar.dropna(subset=['price'])
calendar = calendar[calendar['price'] > 0]

# Rename for merge
calendar.rename(columns={'listing_id': 'listing_id'}, inplace=True)

# === 3. Merge listings with calendar ===
df = pd.merge(calendar, listings, on='listing_id', how='inner')

# Drop rows with missing values after merge
df = df.dropna()

# === 4. Save cleaned data ===
df.to_csv(os.path.join(SAVE_PATH, "merged_airbnb_data.csv"), index=False)
print(f"✅ Cleaned data saved to {os.path.join(SAVE_PATH, 'merged_airbnb_data.csv')}")
