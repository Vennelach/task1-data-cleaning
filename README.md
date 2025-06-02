# task1-data-cleaning
# Netflix Movies and TV Shows - Data Cleaning Project

## Overview
This project involves cleaning and preprocessing the raw Netflix Movies and TV Shows dataset from Kaggle. The goal was to prepare the data for analysis by handling missing values, standardizing formats, removing duplicates, and ensuring data consistency.

## Dataset Source
created a own dataset

## Cleaning Tasks Performed
- **Handled Missing Values:**
  - Filled missing director/cast with "Unknown"
  - Filled missing country with mode value
  - Dropped rows with missing duration or date_added
- **Removed Duplicates:** Eliminated duplicate entries based on title and show_id
- **Standardized Formats:**
  - Converted date_added to datetime format (YYYY-MM-DD)
  - Split duration into numeric value and unit (seasons vs minutes)
  - Standardized country names (e.g., "United States" instead of "US")
- **Data Type Corrections:**
  - Converted show_id to string
  - Ensured release_year as integer
- **Added Derived Columns:**
  - Created "duration_minutes" and "duration_seasons" columns
  - Added "is_movie" flag (True/False)

## Tools Used
- Python 3.x
- Pandas library
- NumPy for numerical operations

## Files Included
- `netflix_cleaning.py`: complete cleaning python code
- `netflix_500_data.csv`: Original raw dataset
- `netflix_500_data_cleaned.csv`: Cleaned dataset

## Key Learnings
- Practical experience with Pandas data cleaning methods
- Understanding common data quality issues in real-world datasets
- Techniques for handling mixed data formats
- Importance of documentation in data preprocessing
