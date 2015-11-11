from pyramid.view import view_config

__author__ = 'yangyang'


@view_config(route_name='home.index', renderer='templates/index.html')
def my_view(request):
    
    return {'project': 'myproject'}
