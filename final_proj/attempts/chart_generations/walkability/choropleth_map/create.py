import plotly.figure_factory as ff
import numpy as np
import pandas as pd

# Load the data
file_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/walkability/processed_data/just_massachusetts/only_Mass.csv'
data = pd.read_csv(file_path)

# Filter the data to include relevant columns
filtered_data = data[['STATEFP', 'COUNTYFP', 'NatWalkInd']]

# Convert STATEFP and COUNTYFP to strings and pad with zeros
filtered_data['STATEFP'] = filtered_data['STATEFP'].apply(lambda x: str(int(x)).zfill(2))
filtered_data['COUNTYFP'] = filtered_data['COUNTYFP'].apply(lambda x: str(int(x)).zfill(3))

# Create FIPS codes
filtered_data['FIPS'] = filtered_data['STATEFP'] + filtered_data['COUNTYFP']

# Sort data by FIPS code (optional, if required)
filtered_data = filtered_data.sort_values('FIPS')

# Define colorscale and endpoints
colorscale = ["#f7fbff", "#ebf3fb", "#deebf7", "#d2e3f3", "#c6dbef", "#b3d2e9", "#9ecae1",
              "#85bcdb", "#6baed6", "#57a0ce", "#4292c6", "#3082be", "#2171b5", "#1361a9",
              "#08519c", "#0b4083", "#08306b"]
endpts = list(np.linspace(filtered_data['NatWalkInd'].min(), filtered_data['NatWalkInd'].max(), len(colorscale) - 1))
fips = filtered_data['FIPS'].tolist()
values = filtered_data['NatWalkInd'].tolist()

# Create the choropleth map
fig = ff.create_choropleth(
    fips=fips, values=values, scope=['massachusetts'],
    binning_endpoints=endpts, colorscale=colorscale,
    show_state_data=False,
    show_hover=True,
    asp=2.9,
    title_text='Massachusetts by Walkability Index',
    legend_title='Walkability Index'
)

fig.layout.template = None

# Save the figure to an HTML file
output_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/chart_generations/walkability/choropleth_map/map.html'
fig.write_html(output_path)

print(f"Choropleth map has been saved to {output_path}")
