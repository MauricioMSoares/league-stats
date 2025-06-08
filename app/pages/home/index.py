from shiny import ui, reactive
from dotenv import load_dotenv
import os

from components.header.index import header_ui
from components.input.index import input_ui
from components.button.index import button_ui


home_ui = ui.page_fluid(
    header_ui(id="home_header"),
    ui.h1("Home"),
    input_ui(id="", input_id="game_name_input", label="Game Name", placeholder="Player"),
    input_ui(id="", input_id="tag_line_input", label="Tag Line", placeholder="#BR1"),
    button_ui(id="", button_id="submit_button", label="Submit"),
)


def home_server(input, output, session):

    @reactive.Effect
    @reactive.event(input.submit_button)
    def submit():
        load_dotenv()
        api_key = os.environ.get("RIOT_API_KEY")
