import pandas as pd
df = pd.read_csv(r"C:\Users\Admin\Downloads\customer_shopping_behavior.csv")

print(df.head())

print(df.info())

print(df.describe(include='all'))

print(df.isnull().sum())

# Detailed missing values analysis
print("\n=== MISSING VALUES ANALYSIS ===")
missing_data = pd.DataFrame({
    'Column': df.columns,
    'Missing_Count': df.isnull().sum(),
    'Missing_Percentage': (df.isnull().sum() / len(df) * 100).round(2)
})
print(missing_data[missing_data['Missing_Count'] > 0])

df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))

print(df.isnull().sum())

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_',regex=False)
df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})

print(df.columns)

# Creating the age column

labels = ['Young Adult', 'Adult', 'Moddle Aged', 'Senoir']
df['age_group'] = pd.qcut(df['age'],q = 4, labels= labels)

print(df[['age','age_group']].head(10))

# Creating column purchase_frequncy_days

frequency_mapping = {
    'Fortnightly' : 14,
    'Weekly' : 7,
    'Monthly' : 30,
    'Quarterly' : 90,
    'Bi_Weekly' : 14,
    'Annually' : 365,
    'Every 3 Months' : 90
}


print(df.columns.tolist())

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping) 

print(df[['purchase_frequency_days', 'frequency_of_purchases']].head(10))

print(df[['discount_applied', 'promo_code_used']].head(10))

print((df['discount_applied'] == df['promo_code_used']).all())

df = df.drop('promo_code_used', axis=1)

print(df.columns)

df.to_csv('cleaned_sales_data.csv', index=False)

print(df)