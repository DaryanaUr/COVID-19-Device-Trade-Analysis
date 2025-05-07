import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('data/fake_trade_data.csv')

# Classify period
def classify_period(year):
    if year <= 2019:
        return 'Pre-COVID'
    elif year in [2020, 2021]:
        return 'During COVID'
    else:
        return 'Post-COVID'

df['Period'] = df['Year'].apply(classify_period)

# Aggregated imports/exports by year
summary = df.groupby('Year')[['Import_Value', 'Export_Value']].sum().reset_index()
plt.figure(figsize=(10,5))
sns.lineplot(data=summary, x='Year', y='Import_Value', label='Imports')
sns.lineplot(data=summary, x='Year', y='Export_Value', label='Exports')
plt.title("Medical Equipment Trade in our country over time")
plt.ylabel("Value (USD)")
plt.grid()
plt.tight_layout()
plt.savefig('plots/trade_over_years.png', dpi=300)
plt.show()

# Imports by category and period
cat_period = df.groupby(['Category', 'Period'])[['Import_Value']].sum().reset_index()
plt.figure(figsize=(10,6))
sns.barplot(data=cat_period, x='Category', y='Import_Value', hue='Period')
plt.title('Imports by Category and Period')
plt.ylabel('Import Value (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('plots/imports_by_category.png', dpi=300)
plt.show()

# Top 10 partners by imports in 2020
top_partners = df[df['Year'] == 2020].groupby('Partner_Country')['Import_Value'].sum().nlargest(10)
top_partners.plot(kind='bar', title='Top Import Partners (2020)', figsize=(8,4))
plt.ylabel("Import Value (USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('plots/top_partners_2020.png', dpi=300)
plt.show()
