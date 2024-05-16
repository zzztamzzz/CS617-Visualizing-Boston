import os
import pandas as pd

# Load the data into a pandas DataFrame
file_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/massbuilds/csv/boston_filtered/massbuilds-20240515.csv'
df = pd.read_csv(file_path)

# Filter the data to include traffic-related projects and extract relevant columns
traffic_related_projects = df[
    (df['traffic_count_data_present'].notnull()) |
    (df['n_transit'].notnull())
][['year_compl', 'status', 'traffic_count_data_present', 'n_transit']]

# Save the filtered data to a new CSV file in the same directory as the input file
filtered_file_path = os.path.join(os.path.dirname(file_path), 'filtered_traffic_related_projects.csv')
traffic_related_projects.to_csv(filtered_file_path, index=False)

print(f'Filtered data saved to {filtered_file_path}')
