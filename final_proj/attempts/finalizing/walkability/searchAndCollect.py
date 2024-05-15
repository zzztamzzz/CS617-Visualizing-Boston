import os
import pandas as pd
from os import path

"""
Original data obtained from https://catalog.data.gov/dataset/walkability-index1
US nation-wide data. Extract Boston relevant data from the original CSV file.
Script to obtain all data entries containing 'Boston' in the original CSV file.
"""

def find_file_path(file_name, search_dir='.'):
    for root, dirs, files in os.walk(search_dir):
        if file_name in files:
            return path.join(root, file_name)
    raise FileNotFoundError(f"File not found: {file_name}")

# Load original data file
search_directory = '.'

# Find the original data file dynamically
original_file_name = 'EPA_SmartLocationDatabase_V3_Jan_2021_Final.csv'
original_df_fp = find_file_path(original_file_name, search_directory)

try:
    original_df = pd.read_csv(original_df_fp)
except FileNotFoundError:
    print(f"File not found: {original_df_fp}")
    exit()

# Print the columns of the original dataframe (optional)
# print(f"\n {original_df.columns} \n")

extracted_dir = path.join(path.dirname(original_df_fp), 'extracted')
os.makedirs(extracted_dir, exist_ok=True)

# Shrink wave 1: Filter and shrink data file to contain only data related to the state of Massachusetts.
# Massachusetts FIPS code is 25
mass_df = original_df[original_df['STATEFP'] == 25]
mass_data_fp = path.join(extracted_dir, 'only_Mass.csv')
mass_df.to_csv(mass_data_fp, index=False)

# Print the columns of the Massachusetts dataframe (optional)
# print(f"\n {mass_df.columns} \n")

print(f'\nExtracted all data associated with Massachusetts. Stored to {mass_data_fp}')

# Shrink wave 2: Narrow down to data related to county.
# Boston is in Suffolk County.
# FIPS code for Suffolk County is 025. In data file, it is listed as 25
suffolk_county_df = mass_df[mass_df['COUNTYFP'] == 25]
sc_data_fp = path.join(extracted_dir, 'only_Suffolk_County.csv')
suffolk_county_df.to_csv(sc_data_fp, index=False)

# Print the columns of the Suffolk County dataframe (optional)
# print(f"\n {suffolk_county_df.columns} \n")

print(f'All Suffolk County data can be found in {sc_data_fp}')

'''
Extracting different columns of data. We have a total of 117 columns :')
Potentially useful columns from data:
#     [Column Name]                [Description of what the column represents]
1.      CBSA_Name           =>         Name of Core-Based Statistical Area
2.      CBSA_POP            =>         Total population of CBSA
3.      CBSA_EMP            =>         Total employment in CBSA
4.      CBSA_WRK            =>         The number of workers in the CBSA
5.      Ac_Total            =>         Total area in acres
6.      TotPop              =>         Population of area
7.      P_WrkAge            =>         Working age population proportion
8.      AutoOwn0            =>         The number of households with zero vehicles.
9.      Pct_AO0             =>         The percentage of households with zero vehicles.
10.     AutoOwn1            =>         The number of households with one vehicle.
11.     Pct_AO1             =>         The percentage of households with one vehicle.
12.     AutoOwn2p           =>         The number of households with two or more vehicles.
13.     Pct_AO2p            =>         The percentage of households with two or more vehicles.
14.     TotEmp              =>         The total number of employed persons.
15.     D2A_JPHH            =>         Jobs per household ratio.
16.     D2C_TRPMX1          =>         Trip mix metric 1.
17.     D2C_TRPMX2          =>         Trip mix metric 2.
18.     D2C_TRIPEQ          =>         Trip equivalency metric 
19.     D2R_JOBPOP          =>         Job to population ratio.
20.     Shape_Length        =>         The length of the geographic shape.
21.     Shape_Area          =>         The area of the geographic shape.
22.     Workers             =>         The total number of workers.
23.     R_LowWageWk         =>         The number of workers earning low wages.
24.     R_MedWageWk         =>         The number of workers earning medium wages.
25.     R_HiWageWk          =>         The number of workers earning high wages
'''

# Potentially useful columns from data:
useful_columns = [
    'CBSA_Name', 'CBSA_POP', 'CBSA_EMP', 'CBSA_WRK', 'Ac_Total', 'TotPop', 'P_WrkAge', 
    'AutoOwn0', 'Pct_AO0', 'AutoOwn1', 'Pct_AO1', 'AutoOwn2p', 'Pct_AO2p', 'TotEmp', 
    'D2A_JPHH', 'D2C_TRPMX1', 'D2C_TRPMX2', 'D2C_TRIPEQ', 'D2R_JOBPOP', 'Shape_Length', 
    'Shape_Area', 'Workers', 'R_LowWageWk', 'R_MedWageWk', 'R_HiWageWk'
]

# Check if all useful columns exist in the dataframe
existing_columns = [col for col in useful_columns if col in suffolk_county_df.columns]
missing_columns = [col for col in useful_columns if col not in suffolk_county_df.columns]

if missing_columns:
    print(f"Warning: Missing columns in data: {missing_columns}")

# Extract useful columns and save to a new file
filtered_columns_df = suffolk_county_df[existing_columns]
filtered_columns_fp = path.join(extracted_dir, 'filtered_Suffolk_County.csv')
filtered_columns_df.to_csv(filtered_columns_fp, index=False)
print(f'Filtered columns saved to {filtered_columns_fp}\n')
