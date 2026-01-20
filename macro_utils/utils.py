import pandas as pd
from .transforms import yoy, mom

def to_scalar(x):
    if hasattr(x, "iloc"):
        return x.iloc[0]
    return x

def build_transformed_dataset(monthly: pd.DataFrame) -> pd.DataFrame:
    """
    Build the canonical transformed macro dataset used across notebooks.

    Produces:
    - GDP_YoY
    - CPI_YoY
    - CPI_MoM
    - UNRATE
    - FEDFUNDS
    """
    df = pd.DataFrame(index=monthly.index)

    df["GDP_YoY"] = yoy(monthly["GDP"])
    df["CPI_YoY"] = yoy(monthly["CPI"])
    df["CPI_MoM"] = mom(monthly["CPI"])
    df["UNRATE"] = monthly["UNRATE"]
    df["FEDFUNDS"] = monthly["FEDFUNDS"]

    return df.dropna()


def prepare_plot_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Reset index and enforce a standard DATE column
    for Plotly compatibility.
    """
    return df.reset_index().rename(columns={"index": "DATE"})


def export_snapshot(snapshot: dict, path):
    """
    Export a single-row snapshot dictionary to CSV.
    """
    pd.DataFrame([snapshot]).to_csv(path, index=False)