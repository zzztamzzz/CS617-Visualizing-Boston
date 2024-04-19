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
# Based on the all-inclusive description, we don't really get any stats for non-numerical values
-> Store all non-numerical values as categorical data
'''
dfCategorize = dfClean2
dfCategorize['POSITION_TITLE'] = dfCategorize['POSITION_TITLE'].astype('category')
dfCategorize['DEPARTMENT_LOCATION_ZIP_CODE'] = dfCategorize['DEPARTMENT_LOCATION_ZIP_CODE'].astype('category')
dfCategorize['Job'] = dfCategorize['Job'].astype('category')
print(dfCategorize.dtypes)
print(dfCategorize.describe(include = 'all'))