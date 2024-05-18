import pandas as pd
import plotly.graph_objects as go

# Load data from CSV files
annual_change_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/population/boston/polished/Boston_Annual_Change.csv'
population_change_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/population/boston/polished/Boston_Population_Change.csv'

annual_change_df = pd.read_csv(annual_change_path)
population_change_df = pd.read_csv(population_change_path)

# Ensure column names are stripped of leading/trailing spaces
annual_change_df.columns = annual_change_df.columns.str.strip()
population_change_df.columns = population_change_df.columns.str.strip()

# Treat 'date' columns as categorical
annual_change_df['date'] = annual_change_df['date'].astype(str)
population_change_df['date'] = population_change_df['date'].astype(str)

# Define custom colors based on Boston-related colors
bar_color = 'rgb(40, 139, 228)'  # Optimistic Blue
line_color = 'rgb(251, 77, 66)'  # Freedom Trail Red
background_color = 'rgb(255, 255, 255)'  # Snow White
grid_color = 'rgb(200, 200, 200)'  # Light grey grid lines

# Create combination chart
fig = go.Figure()

# Add bar chart for population count
fig.add_trace(go.Bar(
    x=population_change_df['date'],
    y=population_change_df['Population'],
    name='Population',
    marker_color=bar_color,
    hoverinfo='x+y',
    text=population_change_df['Population'],
    textposition='outside',
    yaxis='y'
))

# Add line chart for percentage change in population
fig.add_trace(go.Scatter(
    x=annual_change_df['date'],
    y=annual_change_df['Annual Change'],
    name='Annual Change',
    mode='lines+markers',
    line=dict(color=line_color, width=2),  # Thicker line
    marker=dict(size=10, color=line_color),  # Larger markers
    hoverinfo='x+y',
    text=annual_change_df['Annual Change'],
    yaxis='y2'
))

# Update layout for the combination chart
fig.update_layout(
    title=dict(
        text='Population Count and Annual Change Over the Years',
        y=0.95,  # Adjust the title position
        x=0.5,
        xanchor='center',
        yanchor='top',
        font=dict(size=24)  # Larger title font
    ),
    xaxis=dict(
        title='Year',
        showgrid=True,
        gridcolor=grid_color,
        tickangle=45,  # Rotate x-axis labels for better readability
        titlefont=dict(size=18),  # Larger axis title font
        tickfont=dict(size=14)  # Larger axis tick font
    ),
    yaxis=dict(
        title='Population',
        showgrid=True,
        gridcolor=grid_color,
        titlefont=dict(size=18),  # Larger axis title font
        tickfont=dict(size=14)  # Larger axis tick font
    ),
    yaxis2=dict(
        title='Annual Change (%)',
        overlaying='y',
        side='right',
        showgrid=False,
        titlefont=dict(size=18),  # Larger axis title font
        tickfont=dict(size=14)  # Larger axis tick font
    ),
    plot_bgcolor=background_color,
    paper_bgcolor=background_color,
    font=dict(color='rgb(9, 31, 47)'),  # Font color consistent with grid
    margin=dict(l=50, r=50, t=100, b=50),  # Add some margins for better spacing
    hovermode='x unified',  # Unified hover mode for clarity
    hoverlabel=dict(
        bgcolor='white',
        font_size=14,
        font_family='Arial'
    ),
    showlegend=False  # Remove the legend
)

# Save the combination chart as HTML
chart_location = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/chart_generations/population/boston/charts/boston_population_combination_chart.html'
fig.write_html(chart_location)
print(f'Look at this BEAUT {chart_location}')
