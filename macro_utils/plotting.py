import plotly.express as px
import plotly.express as px
import plotly.graph_objects as go

def add_regime_shading(fig, regime_series, opacity=0.08):
    rs = regime_series.dropna()
    if rs.empty:
        return fig

    runs = []
    start = rs.index[0]
    current = rs.iloc[0]

    for dt, val in rs.iloc[1:].items():
        if val != current:
            runs.append((start, dt, current))
            start = dt
            current = val
    runs.append((start, rs.index[-1], current))

    colors = px.colors.qualitative.Set3

    for i, (a, b, _) in enumerate(runs):
        fig.add_vrect(
            x0=a,
            x1=b,
            fillcolor=colors[i % len(colors)],
            opacity=opacity,
            line_width=0,
            layer="below",
        )

    return fig

def plot_timeseries(df, x_col, y_col, title):
    fig = px.line(df, x=x_col, y=y_col, title=title)
    fig.update_layout(height=400)
    fig.show()


def plot_regime_box(df, regime_col, value_col, title):
    fig = px.box(
        df,
        x=regime_col,
        y=value_col,
        points="outliers",
        title=title
    )
    fig.update_layout(height=450)
    fig.show()


def plot_event_study(windows, label, title):
    mean_path = windows.mean()
    p10 = windows.quantile(0.10)
    p90 = windows.quantile(0.90)

    fig = go.Figure()

    for i in range(len(windows)):
        fig.add_trace(go.Scatter(
            x=windows.columns,
            y=windows.iloc[i].values,
            mode="lines",
            opacity=0.15,
            line=dict(width=1),
            showlegend=False
        ))

    fig.add_trace(go.Scatter(
        x=mean_path.index, y=p90.values,
        mode="lines", line=dict(width=0),
        showlegend=False
    ))
    fig.add_trace(go.Scatter(
        x=mean_path.index, y=p10.values,
        fill="tonexty",
        mode="lines",
        line=dict(width=0),
        opacity=0.25,
        name="10–90% band"
    ))
    fig.add_trace(go.Scatter(
        x=mean_path.index,
        y=mean_path.values,
        mode="lines",
        line=dict(width=3),
        name="Mean"
    ))

    fig.add_vline(x=0, line_width=2, line_dash="dash")

    fig.update_layout(
        title=title,
        xaxis_title="Months Relative to Event",
        yaxis_title=label,
        height=500
    )

    fig.show()