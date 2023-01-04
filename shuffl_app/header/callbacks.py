from dash import Input, Output, callback, no_update, State
from shuffl_app.simulation.simulate import simulate_shuffles


@callback(
    Output("config-modal", "opened"),
    Input("config-bttn", "n_clicks"),
    prevent_initial_call=True,
)
def open_close_config_modal(n: int) -> bool:
    return True


@callback(
    Output("config-bttn", "disabled"),
    Input("sim-bttn", "n_clicks"),
    State("number-shuffles", "value"),
    prevent_initial_call=True,
)
def run_simulation(n: int, m: int):

    results = simulate_shuffles(m)

    print(results[0].cards)

    return no_update
