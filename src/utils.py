import pandas as pd

def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^a-z0-9_]", "", regex=True)
    )
    return df

def preview(df: pd.DataFrame, name: str = "DataFrame", n: int = 5) -> None:
    print(f"{name}: {df.shape[0]} rows x {df.shape[1]} cols")
    print(df.head(n))

def fill_with_median(series: pd.Series) -> pd.Series:
    median_value = series.median()
    return series.fillna(median_value)

