import os
import pandas as pd

# Load the data into a pandas DataFrame
file_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/massbuilds/csv/massachusetts/massbuilds-20240515.csv'
df = pd.read_csv(file_path)

# Filter the data to include only completed projects
completed_projects = df[df['status'] == 'completed']

# Extract relevant columns
traffic_related_projects = completed_projects[['year_compl', 'traffic_count_data_present', 'n_transit']]

# Filter projects that have traffic-related data
traffic_related_projects = traffic_related_projects[
    (traffic_related_projects['traffic_count_data_present'].notnull()) |
    (traffic_related_projects['n_transit'].notnull())
]

# Save the filtered data to a new CSV file in the same directory as the input file
filtered_file_path = os.path.join(os.path.dirname(file_path), 'filtered_traffic_related_projects.csv')
traffic_related_projects.to_csv(filtered_file_path, index=False)

print(f'Filtered data saved to {filtered_file_path}')
