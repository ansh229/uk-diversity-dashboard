import pandas as pd
import os
from datetime import datetime

LOG_FILE = "test_log.txt"
DATA_FILE = "figure-6.csv"

# Load and clean data
def load_data():
    try:
        df = pd.read_csv(DATA_FILE)
        df = df.dropna(subset=[df.columns[0], df.columns[1]])
        df.columns = [
            "Title",
            "Group",
            "Region",
            "Contract Type",
            "Job Role",
            "Count"
        ]
        df = df.dropna()
        df = df[df['Count'].apply(lambda x: str(x).isdigit())]
        df['Count'] = df['Count'].astype(int)
        return df, "Pass", "Data loaded and cleaned"
    except Exception as e:
        return None, "Fail", str(e)

# Test 1: Load Data

def test_TC1_load_data():
    return load_data()

# Test 2: Filter by Region

def test_TC2_filter_by_region(df):
    try:
        regions = df['Region'].unique()
        filtered = df[df['Region'] == regions[0]]
        if not filtered.empty:
            return "Pass", "Region filter worked"
        return "Fail", "No data for region filter"
    except Exception as e:
        return "Fail", str(e)

# Test 3: Visualization Check - chart data format

def test_TC3_chart_data(df):
    try:
        group_count = df.groupby("Group")["Count"].sum()
        if group_count.empty:
            return "Fail", "Group count is empty"
        return "Pass", "Chart data grouped successfully"
    except Exception as e:
        return "Fail", str(e)

# Test 4: CSV Export Test

def test_TC4_csv_export(df):
    try:
        df.to_csv("test_export.csv", index=False)
        exists = os.path.exists("test_export.csv")
        return ("Pass", "CSV file exported") if exists else ("Fail", "CSV file not found")
    except Exception as e:
        return "Fail", str(e)

# Test 5: Data Table Preview

def test_TC5_table_preview(df):
    try:
        preview = df.head()
        return ("Pass", "Data previewed") if not preview.empty else ("Fail", "No data in preview")
    except Exception as e:
        return "Fail", str(e)

# Write log

def write_log(entry):
    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")

# Main runner

def run_all_tests():
    tester = "[Your Name]"
    today = datetime.today().strftime('%d-%b-%Y')
    
    df, status1, notes1 = test_TC1_load_data()
    write_log(f"TC1 | {today} | {tester} | {notes1} | {status1}")

    if df is not None:
        status2, notes2 = test_TC2_filter_by_region(df)
        write_log(f"TC2 | {today} | {tester} | {notes2} | {status2}")

        status3, notes3 = test_TC3_chart_data(df)
        write_log(f"TC3 | {today} | {tester} | {notes3} | {status3}")

        status4, notes4 = test_TC4_csv_export(df)
        write_log(f"TC4 | {today} | {tester} | {notes4} | {status4}")

        status5, notes5 = test_TC5_table_preview(df)
        write_log(f"TC5 | {today} | {tester} | {notes5} | {status5}")

if __name__ == "__main__":
    run_all_tests()
    print("All test cases executed. Check test_log.txt for results.")
