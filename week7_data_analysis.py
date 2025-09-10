# -------------------------------
# Import required libraries
# -------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set Seaborn style for attractive plots
sns.set(style="whitegrid")

# =============================================================================
# Task 1: Load and Explore the Dataset
# =============================================================================
print("=== Task 1: Load and Explore Dataset ===")

try:
    # Load Iris dataset
    iris = load_iris()
    
    # Convert to pandas DataFrame
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    
    # Add target column 'species'
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    
    print("Dataset loaded successfully!\n")
    
except Exception as e:
    print(f"Error loading dataset: {e}")

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Display data types and info
print("\nDataset Info:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values per Column:")
print(df.isnull().sum())

# Example of handling missing values (Iris has none)
# df.fillna(method='ffill', inplace=True)  # forward fill
# df.dropna(inplace=True)

print("\nData exploration completed.\n")

# =============================================================================
# Task 2: Basic Data Analysis
# =============================================================================
print("=== Task 2: Basic Data Analysis ===")

# Basic statistics (mean, median, std)
print("Basic Statistics for Numerical Columns:")
print(df.describe())

median_values = df.median()
print("\nMedian values for each numerical column:")
print(median_values)

std_values = df.std()
print("\nStandard deviation for each numerical column:")
print(std_values)

# Grouping by categorical column 'species'
grouped_mean = df.groupby('species').mean()
print("\nMean values for each species:")
print(grouped_mean)

# Observations:
# - Setosa has smaller sepal and petal dimensions than Versicolor and Virginica
# - Virginica generally has the largest petal width and length

# Visualize mean sepal length per species
plt.figure(figsize=(8,5))
grouped_mean['sepal length (cm)'].plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
plt.title("Average Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.xticks(rotation=0)
plt.show()

# =============================================================================
# Task 3: Data Visualization
# =============================================================================
print("=== Task 3: Data Visualization ===")

# 1️⃣ Line Chart (Simulated Trend)
plt.figure(figsize=(8,5))
for species in df['species'].unique():
    subset = df[df['species'] == species]
    plt.plot(subset.index, subset['sepal length (cm)'], marker='o', label=species)
plt.title("Sepal Length Trend by Sample Index")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2️⃣ Bar Chart: Average Petal Length per Species
avg_petal_length = df.groupby('species')['petal length (cm)'].mean()
plt.figure(figsize=(8,5))
avg_petal_length.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.xticks(rotation=0)
plt.show()

# 3️⃣ Histogram: Distribution of Sepal Width
plt.figure(figsize=(8,5))
plt.hist(df['sepal width (cm)'], bins=15, color='purple', edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4️⃣ Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(8,5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, palette='bright', s=100)
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title='Species')
plt.show()

print("\nAll tasks completed. Data analysis and visualizations done!")
