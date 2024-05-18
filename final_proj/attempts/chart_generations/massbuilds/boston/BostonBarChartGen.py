import pandas as pd
import plotly.graph_objects as go

# Load the CSV file
file_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/massbuilds/csv/boston_filtered/processed/boston_filtered_traffic_related_projects.csv'
df = pd.read_csv(file_path)

# Convert cost columns to numeric, handling non-numeric values
df['total_cost'] = pd.to_numeric(df['total_cost'], errors='coerce').fillna(0)

# Categorize the projects
completed_projects = df[df['status'] == 'completed']
planning_projects = df[df['status'] == 'planning']
projected_projects = df[df['status'] == 'projected']
in_construction_projects = df[df['status'] == 'in_construction']
cancelled_projects = df[df['status'] == 'cancelled']

# Count the number of projects completed each year
completed_per_year = completed_projects['year_compl'].value_counts().sort_index()
planning_per_year = planning_projects['year_compl'].value_counts().sort_index()
projected_per_year = projected_projects['year_compl'].value_counts().sort_index()
in_construction_per_year = in_construction_projects['year_compl'].value_counts().sort_index()
cancelled_per_year = cancelled_projects['year_compl'].value_counts().sort_index()

# Calculate total cost of projects for each year
total_cost_per_year = df.groupby('year_compl')['total_cost'].sum()

# Ensure all indices (years) are included in all series for correct stacking
all_years = pd.Index(sorted(set(completed_per_year.index)
                            .union(set(planning_per_year.index))
                            .union(set(projected_per_year.index))
                            .union(set(in_construction_per_year.index))
                            .union(set(cancelled_per_year.index))
                            .union(set(total_cost_per_year.index))))
completed_per_year = completed_per_year.reindex(all_years, fill_value=0)
planning_per_year = planning_per_year.reindex(all_years, fill_value=0)
projected_per_year = projected_per_year.reindex(all_years, fill_value=0)
in_construction_per_year = in_construction_per_year.reindex(all_years, fill_value=0)
cancelled_per_year = cancelled_per_year.reindex(all_years, fill_value=0)
total_cost_per_year = total_cost_per_year.reindex(all_years, fill_value=0)

# Define custom colors for each status
completed_color = '#1f77b4'  # Blue
planning_color = '#ff7f0e'  # Orange
projected_color = '#2ca02c'  # Green
in_construction_color = '#9467bd'  # Purple (swapped with Cancelled)
cancelled_color = '#d62728'  # Red (swapped with In Construction)
cost_color = '#8c564b'  # Brown
background_color = '#FFFFFF'  # Snow White
grid_color = '#E5E5E5'  # Light grey grid lines

# Function to format large numbers with abbreviations
def format_large_numbers(x):
    if x >= 1e9:
        return f'{x / 1e9:.1f}B'
    elif x >= 1e6:
        return f'{x / 1e6:.1f}M'
    elif x >= 1e3:
        return f'{x / 1e3:.1f}K'
    else:
        return str(x)

# Create stacked bar chart
bar_chart = go.Figure()

# Add completed projects trace
bar_chart.add_trace(go.Bar(
    x=completed_per_year.index,
    y=completed_per_year.values,
    name='Completed Projects',
    marker_color=completed_color,
    text=completed_per_year.values,
    textposition='inside',
    insidetextanchor='middle',
    hovertemplate='<b>Year:</b> %{x}<br><b>Completed Projects:</b> %{y}<extra></extra>'
))

# Add planning projects trace
bar_chart.add_trace(go.Bar(
    x=planning_per_year.index,
    y=planning_per_year.values,
    name='Planning Projects',
    marker_color=planning_color,
    text=planning_per_year.values,
    textposition='inside',
    insidetextanchor='middle',
    hovertemplate='<b>Year:</b> %{x}<br><b>Planning Projects:</b> %{y}<extra></extra>'
))

# Add projected projects trace
bar_chart.add_trace(go.Bar(
    x=projected_per_year.index,
    y=projected_per_year.values,
    name='Projected Projects',
    marker_color=projected_color,
    text=projected_per_year.values,
    textposition='inside',
    insidetextanchor='middle',
    hovertemplate='<b>Year:</b> %{x}<br><b>Projected Projects:</b> %{y}<extra></extra>'
))

# Add in construction projects trace (using the color previously assigned to Cancelled)
bar_chart.add_trace(go.Bar(
    x=in_construction_per_year.index,
    y=in_construction_per_year.values,
    name='In Construction Projects',
    marker_color=in_construction_color,
    text=in_construction_per_year.values,
    textposition='inside',
    insidetextanchor='middle',
    hovertemplate='<b>Year:</b> %{x}<br><b>In Construction Projects:</b> %{y}<extra></extra>'
))

# Add cancelled projects trace (using the color previously assigned to In Construction)
bar_chart.add_trace(go.Bar(
    x=cancelled_per_year.index,
    y=cancelled_per_year.values,
    name='Cancelled Projects',
    marker_color=cancelled_color,
    text=cancelled_per_year.values,
    textposition='inside',
    insidetextanchor='middle',
    hovertemplate='<b>Year:</b> %{x}<br><b>Cancelled Projects:</b> %{y}<extra></extra>'
))

# Add total spending trace
bar_chart.add_trace(go.Scatter(
    x=total_cost_per_year.index,
    y=total_cost_per_year.values,
    name='Total Spending',
    mode='lines+markers',
    yaxis='y2',
    marker_color=cost_color,
    line=dict(color=cost_color, width=2),
    hovertemplate='<b>Year:</b> %{x}<br><b>Total Spending:</b> %{text} USD<extra></extra>',
    text=[format_large_numbers(cost) for cost in total_cost_per_year.values],
    textposition='top center'
))

# Update layout for the bar chart
bar_chart.update_layout(
    barmode='stack',
    title=dict(
        text='Number of Traffic-Related Projects and Total Spending by Status Each Year',
        y=0.95,
        x=0.5,
        xanchor='center',
        yanchor='top',
        font=dict(size=24)
    ),
    xaxis=dict(
        title='Year',
        showgrid=True,
        gridcolor=grid_color,
        tickangle=45,
        titlefont=dict(size=18),
        tickfont=dict(size=14)
    ),
    yaxis=dict(
        title='Number of Projects',
        showgrid=True,
        gridcolor=grid_color,
        titlefont=dict(size=18),
        tickfont=dict(size=14)
    ),
    yaxis2=dict(
        title='Total Spending (USD)',
        overlaying='y',
        side='right',
        showgrid=False,
        titlefont=dict(size=18),
        tickfont=dict(size=14),
        tickformat='$,.2f'
    ),
    plot_bgcolor=background_color,
    paper_bgcolor=background_color,
    font=dict(color='#091F2F'),  # Charles Blue for font color
    margin=dict(l=50, r=50, t=100, b=50),
    hovermode='x unified',
    hoverlabel=dict(
        bgcolor='white',
        font_size=14,
        font_family='Arial'
    ),
    showlegend=False  # Remove the legend
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
le_destination = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/chart_generations/massbuilds/boston/boston_projects_bar_chart.html'
bar_chart.write_html(le_destination)
print(f'Done. Feel free.\n {le_destination}')
