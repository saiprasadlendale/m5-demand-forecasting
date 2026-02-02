import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """
    Load Walmart sales dataset and parse dates.
    """
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
    df = df.sort_values("Date")
    return df


def aggregate_company_level(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate weekly sales across all stores (company-level demand).
    """
    company_df = (
        df.groupby("Date", as_index=False)["Weekly_Sales"]
        .sum()
    )
    return company_df
