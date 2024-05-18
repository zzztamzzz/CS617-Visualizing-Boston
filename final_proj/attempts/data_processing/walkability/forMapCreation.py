import pandas as pd

# Load the data
input_file_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/walkability/processed_data/just_massachusetts/filtered_only_mass.csv'
data = pd.read_csv(input_file_path)

# Filter the data to include relevant columns
filtered_data = data[['STATEFP', 'COUNTYFP', 'NatWalkInd']]

# Convert STATEFP and COUNTYFP to strings and pad with zeros
filtered_data['STATEFP'] = filtered_data['STATEFP'].apply(lambda x: str(int(x)).zfill(2))
filtered_data['COUNTYFP'] = filtered_data['COUNTYFP'].apply(lambda x: str(int(x)).zfill(3))

# Create FIPS codes
filtered_data['FIPS'] = filtered_data['STATEFP'] + filtered_data['COUNTYFP']

# Sort data by FIPS code
filtered_data = filtered_data.sort_values('FIPS')

# Save the processed data to a new CSV file
output_file_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/walkability/forMap/map_processed_mass_data.csv'
filtered_data.to_csv(output_file_path, index=False)

print(f"Processed data has been saved to {output_file_path}")
