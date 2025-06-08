from shiny import ui

from components.header.index import header_ui, header_server


home_ui = ui.page_fluid(
    header_ui(id="home_header"),
    ui.h1("Home"),
)


def home_server(input, output, session):
    pass
