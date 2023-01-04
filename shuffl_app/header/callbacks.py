from dash import Input, Output, callback


@callback(Output("config-modal", "opened"), Input("config-bttn", "n_clicks"))
def open_close_config_modal(n: int) -> bool:
    print(n)
    return True
