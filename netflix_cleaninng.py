import pandas as pd
import numpy as np
df = pd.read_csv('netflix_500_data.csv')
print("Initial Data Shape:", df.shape)
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
mode_country = df['country'].mode()[0]
df['country'].fillna(mode_country, inplace=True)
df.dropna(subset=['duration', 'date_added'], inplace=True)
df.drop_duplicates(subset=['title', 'show_id'], keep='first', inplace=True)
# Convert date_added to datetime
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), format='%B %d, %Y')
df['country'] = df['country'].apply(lambda x: 'United States' if x == 'US' else x)
df['duration_numeric'] = df['duration'].str.extract('(\d+)').astype(float)
df['duration_unit'] = df['duration'].str.extract('(min|Season|Seasons)')[0]
df['show_id'] = df['show_id'].astype(str)
df['release_year'] = df['release_year'].astype(int)
df['is_movie'] = df['type'] == 'Movie'
df['duration_minutes'] = np.where(df['type'] == 'Movie', df['duration_numeric'], np.nan)
df['duration_seasons'] = np.where(df['type'] == 'TV Show', df['duration_numeric'], np.nan)
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
print("\nData Types:")
print(df.dtypes)
df.to_csv('netflix_500_data_clean.csv', index=False)

print("\nCleaning complete. Cleaned data saved to 'netflix_500_data_clean.csv'")
print("Final Data Shape:", df.shape)