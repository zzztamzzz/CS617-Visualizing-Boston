import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Directory containing the data files
data_directory = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/walkability/byCounty/specificKeywords'
output_directory_base = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/walkability/plots/byCounty'

# Rename columns
column_rename_map = {
    'CBSA_Name': 'Area',
    'CBSA_POP': 'Population',
    'CBSA_EMP': 'Total Employment',
    'CBSA_WRK': 'Workers in the area',
    'Ac_Total': 'Total area (acres)',
    'Pct_AO0': 'No car owners',
    'Pct_AO1': 'One car owner',
    'Pct_AO2p': '2 or more cars',
    'TotEmp': 'Total people employed',
    'D2R_JOBPOP': 'Job to population ratio',
    'Shape_Length': 'Length of the geographic shape',
    'Shape_Area': 'Area of the geographic shape',
    'R_LowWageWk': 'Low wage workers',
    'R_MedWageWk': 'Medium wage workers',
    'R_HiWageWk': 'High wage workers',
    'D2A_EPHHM': 'Employment per household metric',
    'NatWalkInd': 'National Walkability Index'
}

def create_scatter_plot(df, x_col, y_col, title, x_label, y_label, filename):
    scatter = px.scatter(df, x=x_col, y=y_col, title=title, 
                         labels={x_col: x_label, y_col: y_label},
                         trendline="ols", trendline_color_override='red')
    scatter.update_traces(marker=dict(size=8, opacity=0.5, line=dict(width=1, color='DarkSlateGrey')))
    scatter.update_layout(title_font_size=24, title_x=0.5, xaxis_title_font_size=18, yaxis_title_font_size=18)
    scatter.write_html(filename)
    print(f'Scatter Plot ({title}) saved to: {filename}')

def process_county(file_path, output_directory, county_name):
    # Load the data
    df = pd.read_csv(file_path)
    df.rename(columns=column_rename_map, inplace=True)
    
    # Create scatter plots
    scatter_plots_info = [
        ('Population', 'National Walkability Index', f'Walkability Index vs. Population ({county_name})', 'Population', 'Walkability Index', f'{county_name}_walkability_vs_population.html'),
        ('Total Employment', 'National Walkability Index', f'Walkability Index vs. Employment ({county_name})', 'Employment', 'Walkability Index', f'{county_name}_walkability_vs_employment.html'),
        ('No car owners', 'National Walkability Index', f'Walkability Index vs. No Auto Ownership ({county_name})', 'No Auto Ownership', 'Walkability Index', f'{county_name}_walkability_vs_auto0.html'),
        ('One car owner', 'National Walkability Index', f'Walkability Index vs. One Auto Ownership ({county_name})', 'One Auto Ownership', 'Walkability Index', f'{county_name}_walkability_vs_auto1.html'),
        ('2 or more cars', 'National Walkability Index', f'Walkability Index vs. Two or More Auto Ownership ({county_name})', 'Two or More Auto Ownership', 'Walkability Index', f'{county_name}_walkability_vs_auto2p.html'),
        ('Area of the geographic shape', 'National Walkability Index', f'Walkability Index vs. Shape Area ({county_name})', 'Shape Area', 'Walkability Index', f'{county_name}_walkability_vs_shape_area.html')
    ]

    for x_col, y_col, title, x_label, y_label, filename in scatter_plots_info:
        plot_path = os.path.join(output_directory, filename)
        create_scatter_plot(df, x_col, y_col, title, x_label, y_label, plot_path)
    
    # Bar Chart: Distribution of Wage Workers
    wage_distribution = df[['Low wage workers', 'Medium wage workers', 'High wage workers']].mean()
    bar1 = go.Figure()
    bar1.add_trace(go.Bar(x=wage_distribution.index, y=wage_distribution.values, marker_color=['skyblue', 'orange', 'green']))
    bar1.update_layout(
        title=f'Distribution of Low, Medium, and High-Wage Workers ({county_name})',
        title_font_size=24,
        title_x=0.5,
        xaxis_title='Wage Levels',
        xaxis_title_font_size=18,
        yaxis_title='Number of Workers',
        yaxis_title_font_size=18,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='LightGray')
    )
    bar1_html_path = os.path.join(output_directory, f'{county_name}_wage_distribution.html')
    bar1.write_html(bar1_html_path)
    print(f'Bar Chart (Wage Distribution) saved to: {bar1_html_path}')

# Process all county files
for file_name in os.listdir(data_directory):
    if file_name.startswith('filtered_') and file_name.endswith('_County.csv'):
        file_path = os.path.join(data_directory, file_name)
        county_name = file_name.split('_')[1]
        output_directory = os.path.join(output_directory_base, county_name)
        os.makedirs(output_directory, exist_ok=True)
        print(f'Processing {county_name} County...')
        process_county(file_path, output_directory, county_name)
