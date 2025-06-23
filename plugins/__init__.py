# Don't Remove Credit @T4TVSeries1
# Subscribe YouTube Channel For Amazing Bot @T4TVSeries1
# Ask Doubt on telegram https://t.me/T4TVSeries1

from aiohttp import web
from .route import routes

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
