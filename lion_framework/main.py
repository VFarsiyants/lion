import quopri
from lion_framework.default_views import page_not_found_404
from lion_framework.request_resolver import GetRequest, PostRequest


class LionFramework(GetRequest, PostRequest):
    """
    Класс фреймворка, для инициализации передаем список адресов (маршруты) и
    фронт контроллеры
    """

    def __init__(self, routes: dict, front_controllers: list, settings:dict):
        """
        routes: словарь с ключами - адресами роутов, и значениями - контроллерами
        страниц

        front_controllers: список фронт контроллеров

        settings: настройки запуска веб приложения
        """
        self.routes = routes
        self.front_controllers = front_controllers
        self.settings = settings


    def __call__(self, environ, start_response):
        # адрес с которого поступил запрос
        path = environ['PATH_INFO']

        if self.settings.get('ADD_END_SLASH') == True and not path.endswith('/'):
            path = f'{path}/'

        request = {}
        # получаем тип запроса
        request['method'] = environ['REQUEST_METHOD']

        if request['method'] == 'POST':
            data = self.get_post_request_params(environ)
            request['data'] = data
            print(f'Получен post запрос: \n{LionFramework.decode_value(data)}')
        elif request['method'] == 'GET':
            request['request_params'] = self.get_get_request_params(environ)
            print(f'Получены GET параметры: \n{request["request_params"]}')

        # получаем необходимый контроллер
        if path in self.routes:
            view = self.routes[path]
        else:
            view = page_not_found_404
        
        request = {}

        # фронт контроллеры прогоняют запрос через себя

        for front_controller in self.front_controllers:
            front_controller(request)

        # запускаем контроллер
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace('+', ' '), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data


