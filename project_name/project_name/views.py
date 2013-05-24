from django.template import Context, loader
from django import http
from django.conf import settings


def server_error(request, template_name='500.html'):
    """
    500 error handler.
    """
    t = loader.get_template(template_name)
    return http.HttpResponseServerError(t.render(Context({
        'STATIC_URL': settings.STATIC_URL,
        'request': request,
    })))


def page_error(request, template_name='404.html'):
    """
    404 error handler
    """
    t = loader.get_template(template_name)
    return http.HttpResponseNotFound(t.render(Context({
        'STATIC_URL': settings.STATIC_URL,
        'request': request,
    })))
