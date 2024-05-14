import pandas as pd
import plotly.graph_objects as go
from scipy.spatial import KDTree

# Load data
input_csv_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/finalizing/walkability/boston_walkability_data.csv'
df = pd.read_csv(input_csv_path)

# Extract the specified columns
data = df[['CBSA_POP', 'NatWalkInd', 'Shape_Length', 'Shape_Area']]

# Prepare KDTree for nearest neighbor search
tree = KDTree(data[['CBSA_POP', 'Shape_Length', 'Shape_Area']])

# Initialize figure
fig = go.Figure()

# Example chart creation (this would normally be more dynamic)
values = data[['CBSA_POP', 'Shape_Length', 'Shape_Area']].mean().values
labels = ['CBSA_POP', 'Shape_Length', 'Shape_Area']

fig.add_trace(go.Pie(labels=labels, values=values, hole=.3))
fig.update_layout(title_text='Donut Chart - Walkability Analysis',
                  annotations=[dict(text='Walkability', x=0.5, y=0.5, font_size=20, showarrow=False)])

# Save to HTML file
fig.write_html("/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/finalizing/walkability_chart.html")
