import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the data
file_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/walkability/byCounty/specificKeywords/filtered_Suffolk_County.csv'
df = pd.read_csv(file_path)

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
df.rename(columns=column_rename_map, inplace=True)

# Create output directory path
output_directory = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/walkability/plots/suffolk_county/plots'

# Scatter Plot: Walkability Index vs. Population
scatter1 = px.scatter(df, x='Population', y='National Walkability Index', title='Walkability Index vs. Population', 
                      labels={'Population': 'Population', 'National Walkability Index': 'Walkability Index'},
                      trendline="ols", trendline_color_override='red')
scatter1.update_traces(marker=dict(size=8, opacity=0.5, line=dict(width=1, color='DarkSlateGrey')))
scatter1.update_layout(title_font_size=24, title_x=0.5, xaxis_title_font_size=18, yaxis_title_font_size=18)
scatter1_html_path = f'{output_directory}/walkability_vs_population.html'
scatter1.write_html(scatter1_html_path)
print(f'Scatter Plot (Walkability Index vs. Population) saved to: {scatter1_html_path}')

# Scatter Plot: Walkability Index vs. Employment
scatter2 = px.scatter(df, x='Total Employment', y='National Walkability Index', title='Walkability Index vs. Employment', 
                      labels={'Total Employment': 'Employment', 'National Walkability Index': 'Walkability Index'},
                      trendline="ols", trendline_color_override='red')
scatter2.update_traces(marker=dict(size=8, opacity=0.5, line=dict(width=1, color='DarkSlateGrey')))
scatter2.update_layout(title_font_size=24, title_x=0.5, xaxis_title_font_size=18, yaxis_title_font_size=18)
scatter2_html_path = f'{output_directory}/walkability_vs_employment.html'
scatter2.write_html(scatter2_html_path)
print(f'Scatter Plot (Walkability Index vs. Employment) saved to: {scatter2_html_path}')

# Scatter Plot: Walkability Index vs. Auto Ownership Levels
scatter3 = px.scatter(df, x='No car owners', y='National Walkability Index', title='Walkability Index vs. No Auto Ownership', 
                      labels={'No car owners': 'No Auto Ownership', 'National Walkability Index': 'Walkability Index'},
                      trendline="ols", trendline_color_override='red')
scatter3.update_traces(marker=dict(size=8, opacity=0.5, line=dict(width=1, color='DarkSlateGrey')))
scatter3.update_layout(title_font_size=24, title_x=0.5, xaxis_title_font_size=18, yaxis_title_font_size=18)
scatter3_html_path = f'{output_directory}/walkability_vs_auto0.html'
scatter3.write_html(scatter3_html_path)
print(f'Scatter Plot (Walkability Index vs. No Auto Ownership) saved to: {scatter3_html_path}')

scatter4 = px.scatter(df, x='One car owner', y='National Walkability Index', title='Walkability Index vs. One Auto Ownership', 
                      labels={'One car owner': 'One Auto Ownership', 'National Walkability Index': 'Walkability Index'},
                      trendline="ols", trendline_color_override='red')
scatter4.update_traces(marker=dict(size=8, opacity=0.5, line=dict(width=1, color='DarkSlateGrey')))
scatter4.update_layout(title_font_size=24, title_x=0.5, xaxis_title_font_size=18, yaxis_title_font_size=18)
scatter4_html_path = f'{output_directory}/walkability_vs_auto1.html'
scatter4.write_html(scatter4_html_path)
print(f'Scatter Plot (Walkability Index vs. One Auto Ownership) saved to: {scatter4_html_path}')

scatter5 = px.scatter(df, x='2 or more cars', y='National Walkability Index', title='Walkability Index vs. Two or More Auto Ownership', 
                      labels={'2 or more cars': 'Two or More Auto Ownership', 'National Walkability Index': 'Walkability Index'},
                      trendline="ols", trendline_color_override='red')
scatter5.update_traces(marker=dict(size=8, opacity=0.5, line=dict(width=1, color='DarkSlateGrey')))
scatter5.update_layout(title_font_size=24, title_x=0.5, xaxis_title_font_size=18, yaxis_title_font_size=18)
scatter5_html_path = f'{output_directory}/walkability_vs_auto2p.html'
scatter5.write_html(scatter5_html_path)
print(f'Scatter Plot (Walkability Index vs. Two or More Auto Ownership) saved to: {scatter5_html_path}')

# Scatter Plot: Walkability Index vs. Area of the geographic shape
scatter6 = px.scatter(df, x='Area of the geographic shape', y='National Walkability Index', title='Walkability Index vs. Shape Area', 
                      labels={'Area of the geographic shape': 'Shape Area', 'National Walkability Index': 'Walkability Index'},
                      trendline="ols", trendline_color_override='red')
scatter6.update_traces(marker=dict(size=8, opacity=0.5, line=dict(width=1, color='DarkSlateGrey')))
scatter6.update_layout(title_font_size=24, title_x=0.5, xaxis_title_font_size=18, yaxis_title_font_size=18)
scatter6_html_path = f'{output_directory}/walkability_vs_shape_area.html'
scatter6.write_html(scatter6_html_path)
print(f'Scatter Plot (Walkability Index vs. Shape Area) saved to: {scatter6_html_path}')

# Bar Chart: Distribution of Wage Workers
wage_distribution = df[['Low wage workers', 'Medium wage workers', 'High wage workers']].mean()
bar1 = go.Figure()
bar1.add_trace(go.Bar(x=wage_distribution.index, y=wage_distribution.values, marker_color=['skyblue', 'orange', 'green']))
bar1.update_layout(
    title='Distribution of Low, Medium, and High-Wage Workers',
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
bar1_html_path = f'{output_directory}/wage_distribution.html'
bar1.write_html(bar1_html_path)
print(f'Bar Chart (Wage Distribution) saved to: {bar1_html_path}')
