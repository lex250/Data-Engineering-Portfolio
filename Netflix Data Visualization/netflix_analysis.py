import zipfile
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Extract and Rename the CSV File
# Initialize variables for the zip file path and the extracted file name
zip_file_path = 'netflix_data.zip'
extracted_file_name = 'Netflix_shows_movies.csv'

# Extract the zip file into the current directory
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extract('netflix_data.csv', path='.')
    os.rename('netflix_data.csv', extracted_file_name)

print(f"Extracted file: {extracted_file_name}")

# Step 2: Data Cleaning
# Load the dataset
netflix_data = pd.read_csv(extracted_file_name)

# You can check for missing values to know the columns to fill in. This code is presently commented out to avoid repitition.
#missing_values = netflix_data.isnull().sum()
#print(missing_values)

# Fill missing values with "Unknown" or appropriate placeholders using dictionary approach
netflix_data.fillna({
    'director': 'Unknown',
    'cast': 'Unknown',
    'country': 'Unknown',
    'rating': 'Not Rated',
    'date_added': 'Unknown'
}, inplace=True)

# Verify that all missing values are addressed.
missing_values_cleaned = netflix_data.isnull().sum()
print(f"\nNo missing values after cleaning:\n{missing_values_cleaned}")

# Step 3: Data Exploration
# Generate basic statistics and descriptions of the data
data_description = netflix_data.describe(include='all')
print(f"\nData description:\n{data_description}")

# Step 4: Data Visualization
# Most watched genres
plt.figure(figsize=(14, 8))
genres = netflix_data['listed_in'].str.split(', ').explode()
sns.countplot(y=genres, order=genres.value_counts().index)
plt.title('Most Watched Genres')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.show()

# Ratings distribution
plt.figure(figsize=(12, 6))
sns.countplot(y=netflix_data['rating'], order=netflix_data['rating'].value_counts().index)
plt.title('Ratings Distribution')
plt.xlabel('Count')
plt.ylabel('Rating')
plt.show()