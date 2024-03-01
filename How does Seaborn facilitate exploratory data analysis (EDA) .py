import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
df = pd.read_csv('iris.csv')

# Filter for selected species
selected_species = ['setosa', 'versicolor', 'virginica']
filtered_df = df[df['species'].isin(selected_species)]

# (i) Univariate Analysis on Sepal Length
plt.figure(figsize=(8, 6))
sns.set(style="whitegrid")
sns.histplot(filtered_df, x="sepal_length", hue="species", kde=True, element="step", common_norm=False, palette='Set3')
plt.title('Univariate Analysis: Sepal Length')
plt.show()

# (ii) Bivariate Analysis on Sepal Length and Sepal Width
plt.figure(figsize=(8, 6))
sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=filtered_df, palette='viridis')
plt.title('Bivariate Analysis: Sepal Length vs. Sepal Width')
plt.show()

# (iii) Multivariate Analysis
plt.figure(figsize=(10, 8))
sns.set(style="ticks")
sns.pairplot(filtered_df, hue="species", markers=["o", "s", "D"], palette='viridis')
plt.suptitle('Multivariate Analysis: Sepal Length, Sepal Width, and More', y=1.02)
plt.show()
