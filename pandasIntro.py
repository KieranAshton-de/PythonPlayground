import pandas as pd 
import numpy as np

# Creating empty series 
ser = pd.Series() 
#print("Pandas Series: ", ser) 

# simple array 
data = np.array(['g', 'e', 'e', 'k', 's']) 
  
ser = pd.Series(data) 
print("Pandas Series:\n\n", ser)


# Initializing a DataFrame from a dictionary
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df, "/n")

# Initializing a DataFrame from a list of lists
data = [['John', 25, 'New York'],
        ['Alice', 30, 'Los Angeles'],
        ['Bob', 35, 'Chicago']]
columns = ['Name', 'Age', 'City']
df = pd.DataFrame(data, columns=columns)
print(df)

df['Salary'] = [50000, 60000, 70000]
df = df.set_index('Name')
df = df.reset_index()

avg_age_by_city = df.groupby('City')['Age'].mean()
print('\n *** Average age categories *** \n\n', avg_age_by_city)

df.loc[len(df)] = ["Jenny", 24, "Chicago", 65000]
print(df)

highSalaryEmployees = df[df['Salary'].gt(60000)]
print('\n *** Highest paid employees ***\n', highSalaryEmployees)

highSalaryEmployees = df.query('Salary >= 60000')
print('\n *** Highest paid employees ***\n', highSalaryEmployees)

avg_wage_by_city = df.groupby('City')['Salary'].mean()
avg_wage_in_chicago = avg_wage_by_city.loc['Chicago']
avg_wage_in_chicago2 = avg_wage_by_city.iloc[0:1]
print ('\n *** Average wage in chicago ***\n', avg_wage_in_chicago)
print ('\n *** Average wage in chicago ***\n', avg_wage_in_chicago2)

