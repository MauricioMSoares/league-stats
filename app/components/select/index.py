from shiny import ui, module


@module.ui
def select_ui(select_id: str, label: str, choices: list[tuple[str, str]]):
    return ui.input_select(
        id=select_id,
        label=label,
        choices=choices,
    )


@module.server
def select_server(input, output, session):
    pass
