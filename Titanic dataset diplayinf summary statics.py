import pandas as pd

# Load the Titanic dataset from a CSV file
titanic_data = pd.read_csv('Titanic.csv')

# (i) Select the rows where age of passengers is less than 21 and greater than 40
selected_age_range = titanic_data[(titanic_data['Age'] < 21) | (titanic_data['Age'] > 40)]
print("\n(i) Rows where age is less than 21 or greater than 40:")
print(selected_age_range)

# (ii) Change the age in row for the passenger 12 to 48
titanic_data.loc[titanic_data['PassengerId'] == 12, 'Age'] = 48
print("\n(ii) Age of passenger 12 changed to 48:")

# (iii) Split the dataframe by PClass and get mean, min, and max value of age for each class
class_stats = titanic_data.groupby('Pclass')['Age'].agg(['mean', 'min', 'max'])
print("\n(iii) Statistics by PClass:")
print(class_stats)

# (iv) Replace the mean of age for the missing data
mean_age = titanic_data['Age'].mean()
titanic_data['Age'].fillna(mean_age, inplace=True)
print("\n(iv) Missing age data replaced with mean age:")
