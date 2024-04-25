'''
With the help of pandas, we can do so much processing
In this python script, I have made several changes to the provided csv data file for 'coach_vs_faculty.csv' file
Details for what was done to the file are provided in comments similar to this one.
The script generates 7 separate csv file for each of the processing done to the original data file.
These specific data files are utilized for data for the website visualization
'''
import pandas as pd
df = pd.read_csv('/home/bigboiubu/repos/umb_s24/CS617_Viz/hw4/data/raw/coach_vs_faculty.csv')

# # scanning document raw
# dfHead = df.head()  # first 5 rows
# dfdTypes = df.dtypes # data types
# dfDescribe = df.describe(include='all') # all inclusive summary
# print(dfHead, dfdTypes, dfDescribe)

'''
Checking data file with excel
line 38, PAY_TOTAL_ACTUAL has a 0 value. Could be more and same could be in ANNUAL_RATE

For PAY_TOTAL_ACTUAL column
COUNTIF(D:D, "<0") returned 20 & COUNTIF(D:D, "=0") 1222
Deal with negatives and 0s

For ANNUAL_RATE column, 
we don't have any negatives but we have 0s
COUNTIF(E:E, "<0") returned 0 & COUNTIF(E:E, "=0") returned 25
Deal with 0s only
'''
# there is 1 empty entry in ANNUAL_RATE
# drop 'Unnamed: 0' column and empty cell
dfClean1 = df.drop(columns=['Unnamed: 0'])
dfClean1 = dfClean1.dropna()

# negative values in PAY_TOTAL_ACTUAL
negativePayments = dfClean1[dfClean1['PAY_TOTAL_ACTUAL'] < 0]
zeroPayments = dfClean1[dfClean1['PAY_TOTAL_ACTUAL'] == 0]

# 0 ANNUAL_RATE(s)
zeroRates = dfClean1[dfClean1['ANNUAL_RATE'] == 0]

# print(negativePayments)
# print(zeroPayments)
# print(zeroRates)

# print(dfClean1, dfClean1.describe(include='all')) # still has the negatives

'''
2nd round of cleaning
convert negative entries to their positives
discard zero value entries
'''
dfClean2 = dfClean1
# Convert negative values in 'PAY_TOTAL_ACTUAL' to positive
dfClean2['PAY_TOTAL_ACTUAL'] = dfClean2['PAY_TOTAL_ACTUAL'].abs()

# Remove entries where 'ANNUAL_RATE' is zero
dfClean2 = dfClean2[dfClean2['ANNUAL_RATE'] != 0]
dfClean2 = dfClean2[dfClean2['PAY_TOTAL_ACTUAL'] != 0]

# Checks should return emmpty if done right
negativeCheck = dfClean2[dfClean2['PAY_TOTAL_ACTUAL'] < 0]
noZeroActualCheck = dfClean2[dfClean2['PAY_TOTAL_ACTUAL'] == 0]
annualZeroCheck = dfClean2[dfClean2['ANNUAL_RATE'] == 0]

# print(dfClean2.describe(include='all')) 
# print(negativeCheck, annualZeroCheck, noZeroActualCheck)

'''
Round 3 Categorize
Based on the all-inclusive description, we don't really get any stats for non-numerical values
-> Store all non-numerical values as categorical data
Might come handy later
'''
df_To_categorize = dfClean2
# df_To_categorize['POSITION_TITLE'] = df_To_categorize['POSITION_TITLE'].astype('category')
# df_To_categorize['DEPARTMENT_LOCATION_ZIP_CODE'] = df_To_categorize['DEPARTMENT_LOCATION_ZIP_CODE'].astype('category')
# df_To_categorize['Job'] = df_To_categorize['Job'].astype('category')
# print(df_To_categorize.dtypes)
# print(df_To_categorize.describe(include = 'all'))

# Store clean data into a new csv file.
cleanOut = '/home/bigboiubu/repos/umb_s24/CS617_Viz/hw4/data/processed/CvsF_cleaned.csv'
df_To_categorize.to_csv(cleanOut, index = False)
print("Export done! Cleaned file is ready.")

'''
Organize sum of payroll amounts of each location by year. should be 5 campus locations
Use pivot table and store organized data in a different csv file
'''
# print(df_To_categorize['DEPARTMENT_LOCATION_ZIP_CODE'].unique())

dfYearSum_per_location = df_To_categorize.pivot_table(index = 'YEAR', columns = 'DEPARTMENT_LOCATION_ZIP_CODE', values = 'PAY_TOTAL_ACTUAL', aggfunc = 'sum')
# print(dfYearSum_per_location)
payrollSum_yearly = '/home/bigboiubu/repos/umb_s24/CS617_Viz/hw4/data/processed/Payroll_All_By_Location.csv'
dfYearSum_per_location.to_csv(payrollSum_yearly)
print("File created for sum of payroll[both types] for all locations by the year.")

'''
Organize by position type
Extract 'faculty' for academic and 'coach' for sports
Store in separate files
'''
# print(df_To_categorize['POSITION_TITLE'].unique()) # 252 different positions
# print(df_To_categorize['Job'].unique())
# dfPositionTitle_per_year = data.pivot_table(index='YEAR', columns='POSITION_TITLE', values='PAY_TOTAL_ACTUAL', aggfunc='sum')

academic_data = df_To_categorize[df_To_categorize['Job'] == 'Faculty']
sports_data = df_To_categorize[df_To_categorize['Job'] == 'Coach']
# print(academic_data, sports_data)
# double check
# print(academic_data['Job'].unique())
# print(sports_data['Job'].unique())

# Save the datasets to separate CSV files
academic_file_path = '/home/bigboiubu/repos/umb_s24/CS617_Viz/hw4/data/processed/Academic_Data.csv'
academic_data.to_csv(academic_file_path, index=False)
print("Separated and exported academic positions only.")
sports_file_path = '/home/bigboiubu/repos/umb_s24/CS617_Viz/hw4/data/processed/Sports_Data.csv'
sports_data.to_csv(sports_file_path, index=False)
print("Sports positions are extracted.")

'''
Creating Payroll sum of each job type by the year for all 5 campus locations
Storing them in separate files
'''
# academic_yearly_sum = academic_data.groupby(['YEAR', 'DEPARTMENT_LOCATION_ZIP_CODE'])['PAY_TOTAL_ACTUAL'].sum()
# AYS_fp = '/home/bigboiubu/repos/umb_s24/CS617_Viz/hw4/data/processed/Academic_GroupedYearly_Location.csv'
academic_yearly_sum = academic_data.pivot_table(index = 'YEAR', columns = 'DEPARTMENT_LOCATION_ZIP_CODE', values = 'PAY_TOTAL_ACTUAL', aggfunc = 'sum')
AYS_fp = '/home/bigboiubu/repos/umb_s24/CS617_Viz/hw4/data/processed/Academic_Pivot_Yearly_Location.csv'
academic_yearly_sum.to_csv(AYS_fp)
print("Exported Payroll sum for Academic positions for each loaction for the years")

# repeat for sports
# sports_yearly_sum = sports_data.groupby(['YEAR', 'DEPARTMENT_LOCATION_ZIP_CODE'])['PAY_TOTAL_ACTUAL'].sum()
# SYS_fp = '/home/bigboiubu/repos/umb_s24/CS617_Viz/hw4/data/processed/Sports_GroupedYearly_Location.csv'
sports_yearly_sum = sports_data.pivot_table(index = 'YEAR', columns = 'DEPARTMENT_LOCATION_ZIP_CODE', values = 'PAY_TOTAL_ACTUAL', aggfunc = 'sum')
SYS_fp = '/home/bigboiubu/repos/umb_s24/CS617_Viz/hw4/data/processed/Sports_Pivot_Yearly_Location.csv'
sports_yearly_sum.to_csv(SYS_fp)
print("Sports separated by the year over 5 locations too")

'''
Extract data related to 'YEAR' and 'Job' from the cleaned data
Use this data to show change in employment quantity for 'faculty' vs 'coach' jobs
'''
# print(df_To_categorize['Job'].value_counts())
# print(df_To_categorize['YEAR'].value_counts())
filter_df_by_year_job = df_To_categorize[(df_To_categorize['YEAR'] >= 2010) & (df_To_categorize["YEAR"] <= 2024)]  

employment_trends = filter_df_by_year_job.groupby(['YEAR', 'Job']).size().unstack(fill_value=0)
filter_fp_YvJ = '/home/bigboiubu/repos/umb_s24/CS617_Viz/hw4/data/processed/Filtered_Only_Year_Job.csv'
employment_trends.to_csv(filter_fp_YvJ)
print('We have years and jobs file')
# Get the percentage change, for better viz consumption.
percentage_change = employment_trends.pct_change(periods=1) * 100
percentage_rounded = percentage_change.round(3)
# Replace NaN values with 0 (assumes no change from 2010 as starting point)
percentage_change.iloc[0] = 0
percentage_rounded.iloc[0] = 0

# File path to save the percentage change data
percentage_change_fp = '/home/bigboiubu/repos/umb_s24/CS617_Viz/hw4/data/processed/Percentage_Change_From_2010.csv'
percentage_change.to_csv(percentage_change_fp, index=True)
print("Percentage change from 2010 stored.")

percentage_rounded_fp = '/home/bigboiubu/repos/umb_s24/CS617_Viz/hw4/data/processed/Percentage_Change_Rounded_From_2010.csv'
percentage_rounded.to_csv(percentage_rounded_fp, index=True)