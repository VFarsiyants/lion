from lion_framework.main import LionFramework
from urls import routes, fronts
from wsgiref.simple_server import make_server


settings = {
    'ADD_END_SLASH': True
}

application = LionFramework(routes, fronts, settings)

with make_server('', 8080, application) as server:
    print('Сервер запускается на порту 8080')
    server.serve_forever()
