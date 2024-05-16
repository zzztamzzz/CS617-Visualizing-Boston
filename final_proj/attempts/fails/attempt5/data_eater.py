import pandas as pd
import plotly.express as px

# Load the data into a pandas DataFrame
file_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/attempt5/massbuilds-20240512.csv'
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

# Count the number of traffic-related projects completed each year
traffic_projects_by_year = traffic_related_projects.groupby('year_compl').size().reset_index(name='count')

# Plot the data to visualize the trend over the years using plotly
fig = px.bar(traffic_projects_by_year, x='year_compl', y='count',
             labels={'year_compl': 'Year of Completion', 'count': 'Number of Traffic-related Projects'},
             title='Number of Traffic-related Renovation Projects Completed Over the Years')

# Save the plot to an HTML file
html_file = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/attempt5/traffic_projects_plot.html'
fig.write_html(html_file)

print(f'Plot saved to {html_file}')
