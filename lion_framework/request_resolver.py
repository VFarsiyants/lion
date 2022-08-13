class DataParserMixin:
    def parse_data(self, data:str):
        if data:
            # разбиваем url по ключу и значению
            return {item.split('=')[0]:item.split('=')[1] 
                    for item in data.split('&')}
        return {}


# класс для разбора get запросов
class GetRequest(DataParserMixin):
    def get_get_request_params(self, environ):
        query_string = environ['QUERY_STRING']
        request_params = self.parse_data(query_string)
        return request_params


# класс для разбора POST запросов
class PostRequest(DataParserMixin):
    def get_wsgi_input_data(self, env):
        content_length_data = env.get('CONTENT_LENGTH')
        data = env['wsgi.input'].read(int(content_length_data)) \
               if content_length_data else b''
        return data

    def parse_wsgi_input_data(self, data: bytes):
        if data:
            data_str = data.decode(encoding='utf-8')
            return self.parse_data(data_str)
        return {}

    def get_post_request_params(self, environ):
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        return data
