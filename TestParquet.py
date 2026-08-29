import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import sys
from pathlib import Path

def read_excel_file(excel_path: Path) -> pd.DataFrame:
    if not excel_path.exists():
        raise FileNotFoundError(f"Excel-filen finnes ikke: {excel_path}")
    print(f"[INFO] Leser Excel-fil: {excel_path}")
    df = pd.read_excel(excel_path)
    print(f"[INFO] Antall rader: {len(df)}")
    return df

def validate_dataframe(df: pd.DataFrame):
    print("[INFO] Validerer DataFrame...")
    if df.empty:
        raise ValueError("Excel-filen er tom.")
    if df.columns.isnull().any():
        raise ValueError("Excel-filen har kolonner uten navn.")
    print("[INFO] Validering OK.")

def write_parquet(df: pd.DataFrame, parquet_path: Path):
    print(f"[INFO] Skriver Parquet-fil: {parquet_path}")
    table = pa.Table.from_pandas(df)
    pq.write_table(table, parquet_path)
    print("[INFO] Parquet-fil skrevet.")

def read_parquet(parquet_path: Path) -> pd.DataFrame:
    print(f"[INFO] Leser Parquet-fil: {parquet_path}")
    df = pd.read_parquet(parquet_path)
    print(f"[INFO] Antall rader i Parquet: {len(df)}")
    return df

def main():
    if len(sys.argv) != 3:
        print("Bruk: python excel_to_parquet.py <input.xlsx> <output.parquet>")
        sys.exit(1)

    excel_path = Path(sys.argv[1])
    parquet_path = Path(sys.argv[2])

    df = read_excel_file(excel_path)
    validate_dataframe(df)
    write_parquet(df, parquet_path)

    # Verifisering
    df2 = read_parquet(parquet_path)
    print("[INFO] Første 5 rader fra Parquet:")
    print(df2.head())

if __name__ == "__main__":
    main()
