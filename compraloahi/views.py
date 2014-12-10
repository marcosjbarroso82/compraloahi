from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie



class HomeView(TemplateView):
    template_name = 'index.html'


class ApiDashBoardView(TemplateView):
    template_name = 'api/dashboard.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(ApiDashBoardView, self).dispatch(*args, **kwargs)


class DashBoardView(TemplateView):
    template_name = 'dashboard-ajax.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(DashBoardView, self).dispatch(*args, **kwargs)

class DashBoardAjaxView(TemplateView):
    template_name = 'userProfile/dashboard-ajax.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(DashBoardAjaxView, self).dispatch(*args, **kwargs)