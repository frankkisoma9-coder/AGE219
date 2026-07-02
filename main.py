import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 1. LOAD THE DATA
# We load the CSV and name the columns based on the data structure visible in your file
column_names = ['Domain_Code', 'Domain', 'Element_Code', 'Element', 'Country_Code', 'Country', 'Value', 'Item', 'Year', 'Unit']
df = pd.read_csv('merged_FAOSTAT.csv', names=column_names, header=None, error_bad_lines=False)

# Clean up data: ensure Year and Value are numeric types
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
df = df.dropna(subset=['Year', 'Value'])

# --- 1. TREND ANALYSIS & SCIPY STATISTICAL ANALYSIS ---
yearly_data = df.groupby('Year')['Value'].sum().reset_index()
X = yearly_data['Year']
Y = yearly_data['Value']

# SciPy Linear Regression for the statistical requirement
slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)

plt.figure(figsize=(8, 4))
plt.plot(X, Y, marker='o', color='green', label='Annual Total Value/Prod')
plt.plot(X, slope*X + intercept, color='orange', linestyle='--', label=f'Linear Trend (R={r_value:.2f})')
plt.title('Agricultural Production Dynamics Over Time')
plt.xlabel('Year')
plt.ylabel('Production Metrics [Value]')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig('trend_analysis.png', dpi=300)
plt.close()


# --- 2. CATEGORICAL COMPARISON (BAR CHART) ---
plt.figure(figsize=(10, 5))
# Grouping by 'Item' to see top agricultural categories (e.g., Potatoes, Peas)
category_data = df.groupby('Item')['Value'].sum().sort_values(ascending=False).head(10).reset_index()

sns.barplot(data=category_data, x='Value', y='Item', palette='viridis')
plt.title('Top Agricultural Categories by Value')
plt.xlabel('Total Value')
plt.ylabel('Item Category')
plt.tight_layout()
plt.savefig('categorical_comparison.png', dpi=300)
plt.close()


# --- 3. CORRELATION MAPPING (HEATMAP) ---
plt.figure(figsize=(6, 5))
# Select the numeric columns available for a correlation matrix
numeric_df = df[['Year', 'Value', 'Country_Code']]
correlation_matrix = numeric_df.corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title('Production Metrics Correlation Matrix')
plt.tight_layout()
plt.savefig('correlation_plot.png', dpi=300)
plt.close()

print("All real analysis plots generated successfully!")