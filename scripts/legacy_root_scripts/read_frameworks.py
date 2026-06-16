import pandas as pd
import json

def read_excel(filepath):
    print(f"\n--- Reading {filepath} ---")
    try:
        xl = pd.ExcelFile(filepath)
        for sheet_name in xl.sheet_names:
            print(f"\nSheet: {sheet_name}")
            df = pd.read_excel(filepath, sheet_name=sheet_name)
            # Drop completely empty columns and rows to reduce noise
            df = df.dropna(how='all', axis=1).dropna(how='all', axis=0)
            print(df.to_string(index=False))
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

read_excel(r"C:\Users\aryan\Downloads\Framework_Formatted.xlsx")
read_excel(r"C:\Users\aryan\Downloads\Framework for Interns.xlsx")
