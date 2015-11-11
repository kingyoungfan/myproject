from pyramid.config import Configurator
from pyramid_jinja2 import renderer_factory
from myproject import routers


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.scan()

    routers.includeme(config)
    config.add_renderer('.html', renderer_factory)
    return config.make_wsgi_app()
