from shiny import ui, module


@module.ui
def input_ui(input_id:str, label: str, placeholder: str = None):
    return ui.input_text(
        id=input_id,
        label=label,
        placeholder=placeholder,
    )


@module.server
def input_server(input, output, session):
    pass
