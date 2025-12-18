import pandas as pd
import altair as alt

def styled_histogram(data, title="", x_label="Valeurs", y_label="Fréquence"):
    df = pd.DataFrame({"values": data})

    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X("values", bin=True, title=x_label),
            y=alt.Y("count()", title=y_label)
        )
        .properties(title=title, width=600, height=400)
    )

    return chart
