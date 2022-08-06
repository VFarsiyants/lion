from datetime import date
from views import Index, About


def add_today_front_controller(request):
    request['date'] = date.today()


fronts = [add_today_front_controller]
routes = {
    '/': Index(),
    '/about/': About(),
}
