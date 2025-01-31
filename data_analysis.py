# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load a dataset (replace with your dataset file path)
data = pd.read_csv('sample_dataset.csv')

# Explore the dataset
print("First 5 rows of the dataset:")
print(data.head())

print("\nDataset Info:")
print(data.info())

print("\nSummary Statistics:")
print(data.describe())

# Data manipulation
# Filter rows where a numeric column is greater than a specific value
filtered_data = data[data['Value1'] > 50]
print("\nFiltered Data:")
print(filtered_data)

# Group by a category column and calculate the mean of a numeric column
grouped_data = data.groupby('Category')['Value2'].mean()
print("\nGrouped Data (Mean):")
print(grouped_data)

# Replace missing values with 0
data_filled = data.fillna(0)
print("\nData after filling missing values:")
print(data_filled)
print(data.columns)


# Data Visualization
# 1. Bar Plot for a categorical column
plt.figure(figsize=(8, 5))
data['Category'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Bar Plot of Your Categorical Column")
plt.xlabel("Categories")
plt.ylabel("Count")
plt.savefig('bar_plot.png')  # Save the plot
plt.show()

# 2. Scatter Plot between two numeric columns
plt.figure(figsize=(8, 5))
sns.scatterplot(data=data, x='Value1', y='Value2', color='red')
plt.title("Scatter Plot of Value1 vs Value2")
plt.savefig('scatter_plot.png')  # Save the plot
plt.show()

# 3. Correlation Heatmap
plt.figure(figsize=(10, 8))
correlation = data.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig('correlation_heatmap.png')  # Save the plot
plt.show()
