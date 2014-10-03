import sys
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
# from wsgiref.simple_server import make_server
from waitress import serve

players = {
    'caio': dict(max_hp=57, max_pf=22, max_pm=21,
                 current_hp=57, current_pf=22, current_pm=21),
    'elder': dict(max_hp=36, max_pf=16, max_pm=31,
                  current_hp=36, current_pf=16, current_pm=31),
    'max': dict(max_hp=44, max_pf=36, max_pm=12,
                current_hp=44, current_pf=36, current_pm=12),
    'studart': dict(max_hp=45, max_pf=24, max_pm=20,
                    current_hp=50, current_pf=20, current_pm=20)
}


def root(request):
    return dict(players=players)


def update_hp(request):
    player = request.params['player']
    value = request.params['value']
    players[player]['current_hp'] = int(value)
    return {}


def update_pf(request):
    player = request.params['player']
    value = request.params['value']
    players[player]['current_pf'] = int(value)
    return {}


def update_pm(request):
    # import pdb; pdb.set_trace()
    player = request.params['player']
    value = request.params['value']
    players[player]['current_pm'] = int(value)
    return {}


def create_app():
    config = Configurator()
    config.include('pyramid_jinja2')
    config.add_route('root', '/')
    config.add_view(root, route_name='root', renderer='templates/index.jinja2')

    config.add_route('update_hp', '/update_hp')
    config.add_view(update_hp, route_name='update_hp', renderer='json')

    config.add_route('update_pf', '/update_pf')
    config.add_view(update_pf, route_name='update_pf', renderer='json')

    config.add_route('update_pm', '/update_pm')
    config.add_view(update_pm, route_name='update_pm', renderer='json')

    config.add_static_view(name='static', path='static')
    return config.make_wsgi_app()


if __name__ == '__main__':
    app = create_app()
    try:
        port = sys.argv[1]
    except IndexError:
        port = 8080
    serve(app, host="0.0.0.0", port=port)
