from dash import html
import dash_mantine_components as dmc

title = html.Div(
    [
        dmc.Title("Clustering", weight=600, color="pink", order=5),
        dmc.Text(
            """
            Visualize patterns within the deck.
            """,
            color="dimmed",
            weight=400,
        ),
    ],
    style={"padding-bottom": "10px"},
)


card_right = html.Div(className="card right", children=[title])
