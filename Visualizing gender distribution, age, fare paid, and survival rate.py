import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic_df = pd.read_csv('Titanic.csv')

# (i) Create a pie chart presenting the male/female proportion
gender_counts = titanic_df['Sex'].value_counts()
plt.figure(figsize=(5, 5))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Male/Female Proportion")
plt.show()

# (ii) Create a scatter plot with Fare paid and Age, differentiating by Gender
plt.figure(figsize=(8, 6))
plt.scatter(titanic_df[titanic_df['Sex'] == 'male']['Age'], titanic_df[titanic_df['Sex'] == 'male']['Fare'], c='blue', label='Male', alpha=0.5)
plt.scatter(titanic_df[titanic_df['Sex'] == 'female']['Age'], titanic_df[titanic_df['Sex'] == 'female']['Fare'], c='red', label='Female', alpha=0.5)
plt.xlabel('Age')
plt.ylabel('Fare')
plt.legend()
plt.title('Scatter Plot of Fare vs. Age by Gender')
plt.show()

# (iii) How many people survived?
survived_count = titanic_df['Survived'].sum()
print(f"(iii) Number of people who survived: {survived_count}")

# (iv) Create a histogram with Fare paid
plt.figure(figsize=(8, 6))
plt.hist(titanic_df['Fare'], bins=30, edgecolor='k', alpha=0.7)
plt.xlabel('Fare')
plt.ylabel('Count')
plt.title('Histogram of Fare Paid')
plt.show()
