import pandas as pd

def event_window(series, event_dates, window=12):
    rows = []

    for d in event_dates:
        w = series.loc[
            d - pd.DateOffset(months=window):
            d + pd.DateOffset(months=window)
        ]
        if len(w) == 2 * window + 1:
            w = w.copy()
            w.index = range(-window, window + 1)
            rows.append(w)

    return pd.DataFrame(rows)

def get_contraction_events(macro_regime: pd.Series) -> pd.DatetimeIndex:
    """
    Identify Expansion → Contraction transitions.
    """
    return macro_regime.index[
        macro_regime.shift(1).str.contains("Expansion", na=False)
        & macro_regime.str.contains("Contraction", na=False)
    ]


def pre_post_summary(series: pd.Series, event_dates, window: int = 6) -> pd.DataFrame:
    """
    Compute pre/post averages around event dates.
    """
    records = []

    for d in event_dates:
        if d not in series.index:
            continue

        pre = series.loc[
            d - pd.DateOffset(months=window): d - pd.DateOffset(months=1)
        ].mean()

        post = series.loc[
            d + pd.DateOffset(months=1): d + pd.DateOffset(months=window)
        ].mean()

        records.append({
            "date": d,
            "pre": pre,
            "post": post,
            "delta": post - pre
        })

    return pd.DataFrame(records)