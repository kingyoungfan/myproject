__author__ = 'yangyang'


def includeme(config):
    config.include(home_include, "")


def home_include(config):
    config.add_route("home.index", "/home")
