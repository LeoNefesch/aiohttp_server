from aiohttp import web  # основной модуль aiohttp
import jinja2
import aiohttp_jinja2

from app.settings import config, BASE_DIR
from app.store.database.accessor import PostgresAccessor


def setup_config(application):
    application["config"] = config


def setup_routes(application):
    """Настройка url-путей для всего приложения"""
    from app.forum.routes import setup_routes as setup_forum_routes
    setup_forum_routes(application)


def setup_external_libraries(application):
    aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader(f"{BASE_DIR}/templates"))


def setup_accessors(application):
    application['db'] = PostgresAccessor()
    application['db'].setup(application)


def setup_app(application):
    """Настройка всего приложения"""
    setup_config(application)
    setup_external_libraries(application)
    setup_accessors(application)
    setup_routes(application)


app = web.Application()  # создаем наш веб-сервер

if __name__ == "__main__":
    setup_app(app)  # настраиваем приложение
    web.run_app(app)  # запускаем приложение
