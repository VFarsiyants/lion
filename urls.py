from datetime import date
from views import Index, About, Contact


def add_today_front_controller(request):
    request['today'] = date.today()


fronts = [add_today_front_controller]
routes = {
    '/': Index(),
    '/about/': About(),
    '/contacts/': Contact(),
}
