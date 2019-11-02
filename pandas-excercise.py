import numpy as np
import pandas as pd

sr = pd.read_csv('c:\python37\doc\insurance.csv')

sr.to_string()
#print(sr)
##Print only the column age
#print(sr.age.to_string())

##Print only the column age ,children and charges
sr.columns = ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']
#print(sr[['age', 'children', 'charges']])
##Print only the first 5 lines and only the columns age,children and charges
#print(sr[['age', 'children', 'charges']].head(5))
##What is the average, minimum and maximum charges ?
#print(sr['charges'].mean())
#print(sr['charges'].min())
#print(sr['charges'].max())
##What is the age and sex of the person that paid 10797.3362. Was he/she a smoker

#print(sr.loc[sr['charges'] == 10797.3362])
##What is the age of the person who paid the maximum charge?
#print(sr['charges'].max())
#print(sr.loc[sr['charges'] == 63770.42801])
#print(sr.loc[sr['charges'] == sr['charges'].max()])
#print(sr.index)
#print(sr.columns)
#print(sr.to_sting())
#print(sr['age'])
#print(sr[('charges']))
#match = sr['charges'] == 10797.3362
#print(df[df['charges'] == df['charges'].max()]['age'])

# 10 how many isured people are children
#print(sr[sr['age'] < 18])

#11 and 12 uisng corr(), check if your asumption were correct
#print(sr[['age', 'charges', 'bmi']].corr())

