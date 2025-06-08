from shiny import ui, module
from pathlib import Path


WWW = Path(__file__).resolve() / "../../../www"


@module.ui
def header_ui():
    return ui.tags.header(
        ui.head_content(ui.include_css(WWW / "css/header.css")),
        ui.h1("League Stats"),
        ui.tags.ul(
            ui.tags.li(
                ui.tags.a(
                    ui.span("Home"),
                    href="/home",
                ),
            ),
            ui.tags.li(
                ui.tags.a(
                    ui.span("Dashboard"),
                    href="/dashboard",
                ),
            ),
        ),
    )


@module.server
def header_server(input, output, session):
    pass
