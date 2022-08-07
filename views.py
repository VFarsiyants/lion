from lion_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', data=request.get('data', None))


class Contact:
    def __call__(self, request):
        return '200 OK', render('contacts.html', data=request.get('data', None))


class About:
    def __call__(self, request):
        return '200 OK', 'page about us'
