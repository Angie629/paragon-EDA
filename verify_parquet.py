import pandas as pd
import os

files = [
    r"C:\Users\Angie\Downloads\paragon-eda\dataset\monthly_s1_water_alberta_30km\water_alberta_30km_monthly_2020_2025.parquet",
    r"C:\Users\Angie\Downloads\paragon-eda\dataset\weekly_WITHstorm_SMAP_MODIS_alberta_30km\weekly_storm_smap_modis_2020_2025.parquet"
]

for f in files:
    print(f"\nVerifying {os.path.basename(f)}...")
    if not os.path.exists(f):
        print("ERROR: File not found.")
        continue
    df = pd.read_parquet(f)
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print(f"Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    print("Pre-calculated row counts matches (Monthly=4415, Weekly=285175):", len(df) in [4415, 285175])
