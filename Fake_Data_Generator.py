import pandas as pd
import random
from datetime import datetime

# Output file
output_file = 'data/fake_trade_data.csv'

# Categories and sample products
products = {
    'Respiratory': ['Ventilator', 'Oxygen Mask', 'CPAP Machine'],
    'Imaging': ['X-Ray Machine', 'MRI Scanner', 'Ultrasound'],
    'PPE': ['Surgical Mask', 'Face Shield', 'Gloves'],
    'Injection': ['Syringe', 'Needle', 'IV Set'],
    'Monitoring': ['Pulse Oximeter', 'ECG Monitor', 'Thermometer']
}

years = list(range(2017, 2024))  # 2017–2023
months = list(range(1, 13))      # January–December
partners = ['USA', 'Germany', 'China', 'Japan', 'France', 'Brazil', 'India']

rows = []
for year in years:
    for month in months:
        for category, product_list in products.items():
            for product in product_list:
                row = {
                    'Year': year,
                    'Month': month,
                    'Product': product,
                    'Category': category,
                    'HS_Code': f'9018.{random.randint(10, 99)}',
                    'Import_Value': random.randint(10000, 500000),
                    'Export_Value': random.randint(5000, 300000),
                    'Partner_Country': random.choice(partners)
                }
                rows.append(row)

df = pd.DataFrame(rows)
df.to_csv(output_file, index=False)
print(f"✔️ Fake trade dataset saved to: {output_file}")
