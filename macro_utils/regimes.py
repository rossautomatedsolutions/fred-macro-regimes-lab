import numpy as np
import pandas as pd


# -----------------------
# Core regime classifiers
# -----------------------

def classify_growth(gdp_yoy, threshold=0.0):
    """
    Expansion vs Contraction based on GDP YoY growth.
    """
    return pd.Series(
        np.where(gdp_yoy < threshold, "Contraction", "Expansion"),
        index=gdp_yoy.index,
        name="Growth_Regime"
    )


def classify_inflation(cpi_yoy, threshold=2.5):
    """
    Inflationary vs Disinflationary based on CPI YoY.
    """
    return pd.Series(
        np.where(cpi_yoy > threshold, "Inflationary", "Disinflationary"),
        index=cpi_yoy.index,
        name="Inflation_Regime"
    )


def classify_policy(fedfunds, lookback=12):
    """
    Tightening vs Easing based on rolling rate change.
    """
    rate_change = fedfunds.diff(lookback)

    return pd.Series(
        np.where(rate_change > 0, "Tightening", "Easing"),
        index=fedfunds.index,
        name="Policy_Regime"
    )


# -----------------------
# Regime composition
# -----------------------

def combine_regimes(growth, inflation, policy):
    """
    Combine individual regime components into a composite macro regime.
    """
    return (
        growth + " / " +
        inflation + " / " +
        policy
    ).rename("Macro_Regime")


# -----------------------
# Transitions
# -----------------------

def detect_transitions(series):
    """
    Detect regime transitions in a categorical series.
    """
    prev = series.shift(1)
    mask = (series != prev) & prev.notna()

    return pd.DataFrame({
        "date": series.index[mask],
        "from": prev[mask].values,
        "to": series[mask].values,
    })

def build_macro_regimes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Construct growth, inflation, policy, and combined macro regimes.
    """
    out = df.copy()

    out["Growth_Regime"] = classify_growth(out["GDP_YoY"])
    out["Inflation_Regime"] = classify_inflation(out["CPI_YoY"])
    out["Policy_Regime"] = classify_policy(out["FEDFUNDS"])

    out["Macro_Regime"] = combine_regimes(
        out["Growth_Regime"],
        out["Inflation_Regime"],
        out["Policy_Regime"],
    )

    return out
