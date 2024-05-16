import pandas as pd
import plotly.graph_objects as go

# Load the CSV file
file_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/website_codes/chartGens/massbuilds/filtered_traffic_related_projects.csv'
df = pd.read_csv(file_path)

# Count the number of projects completed each year
projects_per_year = df['year_compl'].value_counts().sort_index()

# Define custom colors
bar_color = 'rgb(34, 139, 34)'  # Forest Green
background_color = 'rgb(245, 245, 245)'  # White Smoke
grid_color = 'rgb(220, 220, 220)'  # Gainsboro

# Create bar chart with enhanced interactivity and visual appeal
bar_chart = go.Figure([go.Bar(
    x=projects_per_year.index,
    y=projects_per_year.values,
    marker_color=bar_color,
    hoverinfo='x+y',
    text=projects_per_year.values,
    textposition='outside',
    hovertemplate='<b>Year:</b> %{x}<br><b>Projects:</b> %{y}<extra></extra>'
)])
bar_chart.update_layout(
    title='Number of Traffic-Related Projects Completed Each Year',
    xaxis_title='Year',
    yaxis_title='Number of Projects',
    plot_bgcolor=background_color,
    paper_bgcolor=background_color,
    font=dict(color='black'),
    xaxis=dict(showgrid=True, gridcolor=grid_color),
    yaxis=dict(showgrid=True, gridcolor=grid_color),
    hovermode='x'
)

# Save bar chart as HTML
le_destination = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/website_codes/chartGens/massbuilds/projects_bar_chart.html'
bar_chart.write_html(le_destination)
print(f'Done. Feel free.\n {le_destination}')