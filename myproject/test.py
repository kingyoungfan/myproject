__author__ = 'yangyang'


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return "Hello World, uwsgi is work!"
