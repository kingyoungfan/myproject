# -*- coding: utf-8 -*-
import os
from pyramid.events import subscriber
from pyramid.events import BeforeRender
from webhelpers.html import literal

URL_PREFIX = '/'


def get_route(*args):
    return os.path.join(URL_PREFIX, *args).replace('\\', '/')


def get_resource(*path):
    return get_route('statics', *path)


@subscriber(BeforeRender)
def add_renderer_globals(event):
    event['t'] = s


def s(request, filep):
    return literal(request.static_url('mypropject:static' + filep))
