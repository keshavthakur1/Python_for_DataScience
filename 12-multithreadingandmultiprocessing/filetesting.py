import pandas as pd

def validate_true_false_excel(filepath):
    try:
        df = pd.read_excel(filepath, engine='openpyxl')
    except ImportError:
        print("❌ 'openpyxl' not installed. Run: pip install openpyxl")
        return
    except Exception as e:
        print(f"❌ Failed to read Excel file: {e}")
        return

    print("\n📋 Detected Columns:", list(df.columns))
    print("\n🔍 First few rows:")
    print(df.head())

    expected_columns = ['Question', 'Answer']
    actual_columns = list(df.columns[:2])

    if actual_columns != expected_columns:
        print(f"\n Invalid column headers.\nExpected: {expected_columns}\nFound: {actual_columns}")
        print(" Check if Row 1 contains 'Question' in A1 and 'Answer' in B1 (not merged or styled).")
        return

    print("✅ Column headers are valid.")

file_path = '12-multithreadingandmultiprocessing/bcatf (1).xlsx'
validate_true_false_excel(file_path)
