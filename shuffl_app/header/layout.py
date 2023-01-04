import dash_mantine_components as dmc
from .elements import logo, config_bttn, config_modal, sim_bttn
from dash import html

bttn_group = dmc.Group(children=[config_bttn, sim_bttn])

header = html.Div(
    className="header",
    children=[dmc.Group([logo, bttn_group], spacing=50, noWrap=True), config_modal],
)
