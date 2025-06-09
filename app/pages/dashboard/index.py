from shiny import ui, reactive

from utils.session_data import session_data


dashboard_ui = ui.page_fluid(ui.h1("Dashboard"))


def dashboard_server(input, output, session):

    @reactive.effect
    def load_data():
        player_info = session_data.get("player_info", {})
        if player_info:
            print("Dashboard received data:", player_info)
        else:
            print("No data found in session data.")
