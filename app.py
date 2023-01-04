from dash import Dash, html
from shuffl_app.header import header
from shuffl_app.content import card_right, card_left

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
)

server = app.server

app.layout = html.Div(
    className="container",
    children=[header, card_left, card_right],
)


if __name__ == "__main__":
    app.run_server(debug=True)
