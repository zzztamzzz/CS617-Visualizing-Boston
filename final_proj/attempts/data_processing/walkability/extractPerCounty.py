import os
import pandas as pd
from os import path

"""
Original data obtained from https://catalog.data.gov/dataset/walkability-index1
US nation-wide data. Extract relevant data for a specified county from the original CSV file.
Script to obtain all data entries containing the specified FIPS code in the original CSV file.
"""

def find_file_path(file_name, search_dir='.'):
    for root, dirs, files in os.walk(search_dir):
        if file_name in files:
            return path.join(root, file_name)
    raise FileNotFoundError(f"File not found: {file_name}")

def get_county_name(fips_code):
    county_names = {
        1: "Barnstable County", 3: "Berkshire County", 5: "Bristol County", 7: "Dukes County", 
        9: "Essex County", 11: "Franklin County", 13: "Hampden County", 15: "Hampshire County", 
        17: "Middlesex County", 19: "Nantucket County", 21: "Norfolk County", 23: "Plymouth County", 
        25: "Suffolk County", 27: "Worcester County"
    }
    return county_names.get(fips_code, f"Unknown_FIPS_{fips_code}")

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def main():
    search_directory = '.'

    # Find the original data file dynamically
    original_file_name = 'EPA_SmartLocationDatabase_V3_Jan_2021_Final.csv'
    try:
        original_df_fp = find_file_path(original_file_name, search_directory)
        original_df = pd.read_csv(original_df_fp)
    except FileNotFoundError as e:
        print(e)
        return

    # Create necessary directories
    base_dir = path.dirname(original_df_fp)
    just_massachusetts_dir = path.join(base_dir, 'just_massachusetts')
    create_directory(just_massachusetts_dir)
    
    extracted_dir = path.join(base_dir, 'byCounty')
    create_directory(extracted_dir)
    create_directory(path.join(extracted_dir, 'all_inclusive'))
    create_directory(path.join(extracted_dir, 'specificKeywords'))

    '''
    Shrink wave 1 
    Filter and shrink data file to contain only data related to the state of Massachusetts.
    Massachusetts FIPS code is 25
    '''
    mass_df = original_df[original_df['STATEFP'] == 25]
    mass_data_fp = path.join(just_massachusetts_dir, 'only_Mass.csv')
    mass_df.to_csv(mass_data_fp, index=False)

    print(f'Extracted all data associated with Massachusetts. Stored to {mass_data_fp}\n')
    '''
    Shrink wave 2 
    Narrow down to data related to county.
    Boston is in Suffolk County.
    FIPS code for Suffolk County is 025. In data file, it is listed as 25
    May as well get the other counties too.
    '''
    county_fips_codes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]
    useful_columns = [
        'CBSA_Name', 'CBSA_POP', 'CBSA_EMP', 'CBSA_WRK', 'Ac_Total', 'Pct_AO0', 'Pct_AO1', 
        'Pct_AO2p', 'TotEmp', 'D2R_JOBPOP', 'Shape_Length', 'Shape_Area', 'Workers', 'R_LowWageWk',
        'R_MedWageWk', 'R_HiWageWk', 'D2A_EPHHM', 'NatWalkInd'
    ]

    for county_fips_code in county_fips_codes:
        county_name = get_county_name(county_fips_code)
        county_df = mass_df[mass_df['COUNTYFP'] == county_fips_code]
        county_data_fp = path.join(extracted_dir, f'all_inclusive/{county_name.replace(" ", "_")}_data.csv')
        county_df.to_csv(county_data_fp, index=False)
        print(f'All {county_name} data can be found in {county_data_fp}')
        
        existing_columns = [col for col in useful_columns if col in county_df.columns]
        missing_columns = [col for col in useful_columns if col not in county_df.columns]
        
        if missing_columns:
            print(f"Warning: Missing columns in {county_name} data: {missing_columns}")
        
        filtered_columns_df = county_df[existing_columns]
        filtered_columns_fp = path.join(extracted_dir, f'specificKeywords/filtered_{county_name.replace(" ", "_")}.csv')
        filtered_columns_df.to_csv(filtered_columns_fp, index=False)
        print(f'Filtered columns for {county_name} saved to {filtered_columns_fp}\n')
        # print(filtered_columns_df.describe()) 

if __name__ == "__main__":
    main()


'''
Extracting different columns of data from the original file. We have a total of 117 columns :')
Potentially useful columns from data:
#     [Column Name]             [Description of what the column represents]                 ['X' means not using]
1.      CBSA_Name       =>          Name of Core-Based Statistical Area
2.      CBSA_POP        =>          Total population of CBSA
3.      CBSA_EMP        =>          Total employment in CBSA
4.      CBSA_WRK        =>          The number of workers in the CBSA                                
5.      Ac_Total        =>          Total area in acres
6.      TotPop          =>          Population of area
7.      P_WrkAge        =>          Working age population proportion                                X           
8.      AutoOwn0        =>          The number of households with zero vehicles.                     X
9.      Pct_AO0         =>          The percentage of households with zero vehicles.                 
10.     AutoOwn1        =>          The number of households with one vehicle.                       X        
11.     Pct_AO1         =>          The percentage of households with one vehicle.
12.     AutoOwn2p       =>          The number of households with two or more vehicles.              X
13.     Pct_AO2p        =>          The percentage of households with two or more vehicles.              
14.     TotEmp          =>          The total number of employed persons.
15.     D2A_JPHH        =>          Jobs per household ratio.                                        X
16.     D2C_TRPMX1      =>          Trip mix metric 1.                                               X
17.     D2C_TRPMX2      =>          Trip mix metric 2.                                               X
18.     D2C_TRIPEQ      =>          Trip equivalency metric                                          X
19.     D2R_JOBPOP      =>          Job to population ratio.
20.     Shape_Length    =>          The length of the geographic shape.
21.     Shape_Area      =>          The area of the geographic shape.
22.     Workers         =>          The total number of workers.                                     X
23.     R_LowWageWk     =>          The number of workers earning low wages.
24.     R_MedWageWk     =>          The number of workers earning medium wages.
25.     R_HiWageWk      =>          The number of workers earning high wages.
26.     D2A_EPHHM       =>          Employment per household metric
27.     NatWalkInd      =>          National Walkability Index 
'''
