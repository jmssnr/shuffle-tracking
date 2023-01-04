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
    children=[],
    size="lg",
)
