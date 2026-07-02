import pandas as pd
import matplotlib.pyplot as plt
  # <--- DELETE THIS ENTIRE LINE!
from scipy import stats

# 1. LOAD THE DATA
df = pd.read_csv('merged_FAOSTAT.csv', on_bad_lines="skip")

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
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# 1. LOAD THE DATA
column_names = ['Domain_Code', 'Domain', 'Element_Code', 'Element', 'Country_Code', 'Country', 'Value', 'Item', 'Year', 'Unit']
df = pd.read_csv('merged_FAOSTAT.csv', names=column_names, header=None, on_bad_lines="skip")

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


# --- 2. CATEGORICAL COMPARISON (BAR CHART - WITHOUT SEABORN) ---
plt.figure(figsize=(10, 5))
# Grouping by 'Item' to see top agricultural categories (e.g., Potatoes, Peas)
category_data = df.groupby('Item')['Value'].sum().sort_values(ascending=False).head(10).reset_index()

# Using standard matplotlib barh instead of seaborn barplot
plt.barh(category_data['Item'], category_data['Value'], color='#440154')
plt.gca().invert_yaxis()  # Put the highest value at the top
plt.title('Top Agricultural Categories by Value')
plt.xlabel('Total Value')
plt.ylabel('Item Category')
plt.tight_layout()
plt.savefig('categorical_comparison.png', dpi=300)
plt.close()


# --- 3. CORRELATION MAPPING (MATRIX DISPLAY - WITHOUT SEABORN) ---
plt.figure(figsize=(6, 5))
numeric_df = df[['Year', 'Value', 'Country_Code']]
correlation_matrix = numeric_df.corr()

# Using standard matplotlib matshow to create a heatmap grid
alpha_labels = correlation_matrix.columns
fig, ax = plt.subplots(figsize=(6, 5))
cax = ax.matshow(correlation_matrix, cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)

# Add correlation values as text inside the squares
for i in range(len(alpha_labels)):
    for j in range(len(alpha_labels)):
        text = ax.text(j, i, f"{correlation_matrix.iloc[i, j]:.2f}",
                       ha="center", va="center", color="black" if abs(correlation_matrix.iloc[i, j]) < 0.7 else "white")

ax.set_xticks(range(len(alpha_labels)))
ax.set_yticks(range(len(alpha_labels)))
ax.set_xticklabels(alpha_labels)
ax.set_yticklabels(alpha_labels)
plt.title('Production Metrics Correlation Matrix', pad=20)
plt.tight_layout()
plt.savefig('correlation_plot.png', dpi=300)
plt.close()

print("All real analysis plots generated successfully offline!")
