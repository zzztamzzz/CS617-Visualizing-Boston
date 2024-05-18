import pandas as pd
import os

def clean_population_data(file_path):
    # Load the data, skipping initial non-data lines
    data = pd.read_csv(file_path, skiprows=15)
    
    # Remove any leading/trailing whitespace from column names
    data.columns = data.columns.str.strip()
    
    # Convert 'date' column to datetime
    data['date'] = pd.to_datetime(data['date'])
    
    # Filter data to include only up to the year 2023
    data = data[data['date'].dt.year <= 2035]
    
    # Handle missing values in 'Annual Change' by filling them with the median
    median_annual_change = data['Annual Change'].median()
    data['Annual Change'] = data['Annual Change'].fillna(median_annual_change)
    
    return data

# Path to the CSV file
file_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/population/boston/original/Boston-population-2024-05-15.csv'

# Clean the data
cleaned_data = clean_population_data(file_path)

# Create 'polished' directory if it doesn't exist
polished_dir = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/population/boston/polished'
os.makedirs(polished_dir, exist_ok=True)

# Define the file path to save the cleaned data in the 'polished' directory
output_file_path = os.path.join(polished_dir, 'Boston_Population_Data.csv')

# Save the data to a new CSV file in the 'polished' directory
cleaned_data.to_csv(output_file_path, index=False)

print(f"Cleaned data saved to {output_file_path}")
