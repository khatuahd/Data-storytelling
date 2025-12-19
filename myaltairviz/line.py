import pandas as pd
import altair as alt

def styled_line(x, y, title="", x_label="X", y_label="Y"):
    df = pd.DataFrame({"x": x, "y": y})

    chart = (
        alt.Chart(df)
        .mark_line(point=True, strokeWidth=3)
        .encode(
            x=alt.X("x", title=x_label),
            y=alt.Y("y", title=y_label)
        )
        .properties(title=title, width=600, height=400)
    )

    return chart
