import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

config_bttn = dmc.Button(
    "Configure",
    id="config-bttn",
    color="pink",
    variant="light",
    leftIcon=DashIconify(icon="material-symbols:settings-outline-rounded"),
)

sim_bttn = dmc.Button(
    "Simulate",
    id="sim-bttn",
    color="pink",
    variant="light",
    leftIcon=DashIconify(icon="material-symbols:shuffle"),
)

logo = html.Img(src="assets/shuffl-logo.png", height="90px")

config_modal = dmc.Modal(
    id="config-modal",
    title=dmc.Title("Configure Simulation", weight=600, color="pink", order=5),
    children=[
        dmc.Group(
            [
                dmc.Select(
                    id="deck-order-picker",
                    label="Starting deck order",
                    icon=DashIconify(icon="mdi:cards"),
                    data=[
                        {"label": "New deck order", "value": "ndo"},
                    ],
                    value="ndo",
                ),
                dmc.Select(
                    id="shuffle-picker",
                    label="Shuffle type",
                    icon=DashIconify(icon="mdi:cards-variant"),
                    data=[
                        {"label": "Riffle shuffle", "value": "riffle"},
                    ],
                    value="riffle",
                ),
                dmc.NumberInput(
                    id="number-shuffles",
                    label="Number of repetitions",
                    description="From 100 to 1000000, in steps of 100",
                    value=1000,
                    min=100,
                    max=1000000,
                    step=100,
                    style={"width": 250},
                ),
            ]
        )
    ],
    size="lg",
)
