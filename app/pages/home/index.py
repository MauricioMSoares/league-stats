from shiny import ui, reactive
from dotenv import load_dotenv
import os
import httpx

from components.header.index import header_ui
from components.input.index import input_ui
from components.select.index import select_ui
from components.button.index import button_ui
from utils.session_data import session_data
from data.game_servers import servers_dict, region_by_server


home_ui = ui.page_fluid(
    header_ui(id="home_header"),
    ui.h1("Home"),
    input_ui(
        id="", input_id="game_name_input", label="Game Name", placeholder="Player"
    ),
    input_ui(id="", input_id="tag_line_input", label="Tag Line #", placeholder="BR1"),
    select_ui(
        id="",
        select_id="server_select",
        label="Server",
        choices=servers_dict,
    ),
    button_ui(id="", button_id="submit_button", label="Submit"),
)


def home_server(input, output, session):

    @reactive.Effect
    @reactive.event(input.submit_button)
    async def submit():
        load_dotenv()
        game_name = input.game_name_input()
        tag_line = input.tag_line_input()
        server = input.server_select()
        region = region_by_server.get(server)
        api_key = os.environ.get("RIOT_API_KEY")
        url = f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}?api_key={api_key}"
        puuid = await fetch_puuid(url)
        update_session_data(game_name, tag_line, server, puuid)

    async def fetch_puuid(url: str):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url)
                response.raise_for_status()  # Raise error for bad status codes
                data = response.json()
                puuid = data["puuid"]
                ui.notification_show(
                    "Player info fetched successfully!", type="message"
                )
                return puuid
            except httpx.HTTPStatusError as e:
                ui.notification_show(
                    f"HTTP error: {e.response.status_code}", type="error"
                )
            except Exception as e:
                ui.notification_show(f"Error: {str(e)}", type="error")

    def update_session_data(game_name: str, tag_line: str, server: str, puuid: str):
        session_data["player_info"] = {
            "game_name": game_name,
            "tag_line": tag_line,
            "server": server,
            "puuid": puuid,
        }
