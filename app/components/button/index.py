from shiny import ui, module


@module.ui
def button_ui(button_id: str, label: str):
    return ui.input_action_button(
        id=button_id,
        label=label,
    )


@module.server
def button_server(input, output, session):
    pass
