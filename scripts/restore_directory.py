import pandas as pd

# Load directory
df = pd.read_csv('mp_forest_directory.csv', encoding='utf-8-sig')

# Slice the first 420 rows (indices 0 to 419) which are the original real scraped data
original_df = df.iloc[:420]

# Save back to CSV
original_df.to_csv('mp_forest_directory.csv', index=False, encoding='utf-8-sig')

print(f"Directory restored successfully to {len(original_df)} real rows!")
