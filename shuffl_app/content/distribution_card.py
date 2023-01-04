from dash import html
import dash_mantine_components as dmc
from shuffl_app.simulation import Deck


title = html.Div(
    [
        dmc.Title("Distribution", weight=600, color="pink", order=5),
        dmc.Text(
            """
            Select up to 5 cards and visualize their distribution within
            the deck.
            """,
            color="dimmed",
            weight=400,
        ),
    ],
    style={"padding-bottom": "10px"},
)


card_left = html.Div(className="card left", children=[title, Deck().reveal()])
