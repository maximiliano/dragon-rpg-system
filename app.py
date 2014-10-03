import sys
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
# from wsgiref.simple_server import make_server
from waitress import serve

players = {
    'caio': dict(hp=57, pf=22, pm=21),
    'elder': dict(hp=36, pf=16, pm=31),
    'max': dict(hp=44, pf=36, pm=12),
    'studart': dict(hp=50, pf=20, pm=20)
}

def root(request):
    return dict(players=players)


# @view_config(route_name='hello_json', renderer='json')
# def hello_json(request):
#     return [1, 2, 3]
#     # End View 1


def create_app():
    config = Configurator()
    config.include('pyramid_jinja2')
    config.add_route('root', '/')
    config.add_static_view(name='static', path='static')
    config.add_view(root, route_name='root', renderer='templates/index.jinja2')
    return config.make_wsgi_app()


if __name__ == '__main__':
    app = create_app()
    try:
        port = sys.argv[1]
    except IndexError:
        port = 8080
    serve(app, host="0.0.0.0", port=port)
