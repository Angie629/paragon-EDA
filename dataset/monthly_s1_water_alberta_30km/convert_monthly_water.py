import pandas as pd
import glob
import os

# Configuration
input_dir = r"C:\Users\Angie\Downloads\paragon-eda\dataset\monthly_s1_water_alberta_30km"
output_file = os.path.join(input_dir, "water_alberta_30km_monthly_2020_2025.parquet")
file_pattern = os.path.join(input_dir, "s1_water_alberta_30km_monthly_*.csv")

def main():
    print(f"Searching for CSV files in: {input_dir}")
    csv_files = sorted(glob.glob(file_pattern))
    
    if not csv_files:
        print("No CSV files found matching the pattern.")
        return

    print(f"Found {len(csv_files)} files.")

    df_list = []
    for file in csv_files:
        print(f"Reading {os.path.basename(file)}...")
        df = pd.read_csv(file)
        
        # Ensure '.geo' is handled as string if present
        if '.geo' in df.columns:
            df['.geo'] = df['.geo'].astype(str)
            
        # Ensure 'ym' is handled as string
        if 'ym' in df.columns:
            df['ym'] = df['ym'].astype(str)
            
        df_list.append(df)

    print("Concatenating DataFrames...")
    combined_df = pd.concat(df_list, ignore_index=True)

    print(f"Writing to Parquet: {output_file}")
    combined_df.to_parquet(output_file, engine='pyarrow', index=False)
    
    print("Conversion complete!")
    print(f"Total rows: {len(combined_df)}")

if __name__ == "__main__":
    main()
