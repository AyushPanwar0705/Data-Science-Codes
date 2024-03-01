import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
df = pd.read_csv('iris.csv')

# Seaborn Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal_length', y='sepal_width', data=df, hue='species', palette='viridis')
plt.title('Seaborn Scatter Plot')
plt.show()

# Matplotlib Scatter Plot
plt.figure(figsize=(8, 6))
colors = {'setosa': 'r', 'versicolor': 'g', 'virginica': 'b'}
plt.scatter(df['sepal_length'], df['sepal_width'], c=[colors[x] for x in df['species']])
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.title('Matplotlib Scatter Plot')
plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='r', label='setosa', markersize=8),
                    plt.Line2D([0], [0], marker='o', color='g', label='versicolor', markersize=8),
                    plt.Line2D([0], [0], marker='o', color='b', label='virginica', markersize=8)])
plt.show()
