import pandas as pd

def clean_population_data(file_path):
    # Load the data, skipping initial non-data lines
    data = pd.read_csv(file_path, skiprows=15)
    
    # Remove any leading/trailing whitespace from column names
    data.columns = data.columns.str.strip()
    
    # Convert 'date' column to datetime and then extract only the year
    data['date'] = pd.to_datetime(data['date']).dt.year
    
    # Filter data to include only up to the year 2023
    data = data[data['date'] <= 2023]
    
    # Handle missing values in 'Annual Change' by filling them with the median
    median_annual_change = data['Annual Change'].median()
    data['Annual Change'] = data['Annual Change'].fillna(median_annual_change)
    
    return data

# Path to the CSV file
file_path = '/home/bigboiubu/fresh_data/population/Boston-population-2024-05-12.csv'

# Clean the data
cleaned_data = clean_population_data(file_path)

# Creating two separate dataframes for different outputs
data_population_change = cleaned_data[['date', 'Population']]
data_annual_change = cleaned_data[['date', 'Annual Change']]

# Save the data to new CSV files
output_file_path_pop_change = '/home/bigboiubu/fresh_data/population/Population_Change.csv'
output_file_path_annual_change = '/home/bigboiubu/fresh_data/population/Annual_Change.csv'

data_population_change.to_csv(output_file_path_pop_change, index=False)
data_annual_change.to_csv(output_file_path_annual_change, index=False)

print(f"Population Change data saved to {output_file_path_pop_change}")
print(f"Annual Change data saved to {output_file_path_annual_change}")
