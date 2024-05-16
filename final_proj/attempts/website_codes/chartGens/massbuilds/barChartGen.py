import pandas as pd
import plotly.graph_objects as go

# Load the CSV file
file_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/website_codes/chartGens/massbuilds/filtered_traffic_related_projects.csv'
df = pd.read_csv(file_path)

# Categorize the projects
completed_projects = df[df['status'] == 'completed']
other_projects = df[df['status'] != 'completed']

# Count the number of projects completed each year
completed_per_year = completed_projects['year_compl'].value_counts().sort_index()
other_per_year = other_projects['year_compl'].value_counts().sort_index()

# Ensure all indices (years) are included in both series for correct stacking
all_years = pd.Index(sorted(set(completed_per_year.index).union(set(other_per_year.index))))
completed_per_year = completed_per_year.reindex(all_years, fill_value=0)
other_per_year = other_per_year.reindex(all_years, fill_value=0)

# Calculate the average number of projects
average_projects = completed_per_year.mean()

# Define custom colors
completed_color = 'rgb(34, 139, 34)'  # Forest Green
other_color = 'rgb(255, 165, 0)'  # Orange
background_color = 'rgb(250, 250, 250)'  # Light Gray
grid_color = 'rgb(220, 220, 220)'  # Very Light Gray
average_line_color = 'rgb(0, 0, 0)'  # Black

# Create stacked bar chart
bar_chart = go.Figure()

# Add completed projects trace
bar_chart.add_trace(go.Bar(
    x=completed_per_year.index,
    y=completed_per_year.values,
    name='Completed Projects',
    marker_color=completed_color,
    hoverinfo='x+y',
    text=completed_per_year.values,
    textposition='outside',
    hovertemplate='<b>Year:</b> %{x}<br><b>Completed Projects:</b> %{y}<extra></extra>'
))

# Add other projects trace
bar_chart.add_trace(go.Bar(
    x=other_per_year.index,
    y=other_per_year.values,
    name='Other Projects',
    marker_color=other_color,
    hoverinfo='x+y',
    text=other_per_year.values,
    textposition='outside',
    hovertemplate='<b>Year:</b> %{x}<br><b>Other Projects:</b> %{y}<extra></extra>'
))

# Add a dashed line for the average number of projects
bar_chart.add_trace(go.Scatter(
    x=completed_per_year.index,
    y=[average_projects] * len(completed_per_year),
    mode='lines',
    name='Average Projects',
    line=dict(color=average_line_color, width=2, dash='dash'),
    hovertemplate='<b>Average Projects:</b> %{y:.2f}<extra></extra>'
))

# Update layout for the bar chart
bar_chart.update_layout(
    barmode='stack',
    title='Number of Traffic-Related Projects Completed and Other Projects Each Year',
    xaxis_title='Year',
    yaxis_title='Number of Projects',
    plot_bgcolor=background_color,
    paper_bgcolor=background_color,
    font=dict(color='black'),
    xaxis=dict(showgrid=True, gridcolor=grid_color),
    yaxis=dict(showgrid=True, gridcolor=grid_color),
    hovermode='x'
)

# Add a range slider for filtering the years
bar_chart.update_layout(
    xaxis=dict(
        rangeslider=dict(
            visible=True,
            thickness=0.1,
            bgcolor='rgb(200, 200, 200)'
        ),
        type="linear"
    )
)

# Save bar chart as HTML
le_destination = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/website_codes/chartGens/massbuilds/projects_bar_chart.html'
bar_chart.write_html(le_destination)
print(f'Done. Feel free.\n {le_destination}')
