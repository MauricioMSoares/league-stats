from shiny import App
from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.responses import RedirectResponse

from pages.home.index import home_ui, home_server
from pages.dashboard.index import dashboard_ui, dashboard_server


home_app = App(home_ui, home_server)
dashboard_app = App(dashboard_ui, dashboard_server)


async def home(request):
    return RedirectResponse(url="/home")


routes = [
    Route("/", endpoint=home),
    Mount("/home", app=home_app),
    Mount("/dashboard", app=dashboard_app),
]


app = Starlette(routes=routes)
