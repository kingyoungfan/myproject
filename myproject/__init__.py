import os
from pyramid.config import Configurator
from pyramid_jinja2 import renderer_factory
from myproject import routers

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.scan()

    routers.includeme(config)

    config.add_translation_dirs('myproject:locale')
    config.include('pyramid_jinja2')
    config.add_renderer('.html', renderer_factory)
    config.add_static_view('static', 'myproject:static', cache_max_age=3600)
    return config.make_wsgi_app()
