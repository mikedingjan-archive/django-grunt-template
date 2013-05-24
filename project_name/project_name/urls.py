from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

handler500 = '{{ project_name }}.views.server_error'
handler404 = '{{ project_name }}.views.page_error'


urlpatterns = patterns(
    '',
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('project_name.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if getattr(settings, 'DEBUG', False):
    from django.core.urlresolvers import get_resolver

    errorresolve = get_resolver(None)
    urlpatterns += patterns(
        '',
        url(r'500/$', *errorresolve.resolve500()),
        url(r'404/$', *errorresolve.resolve404()),

        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True
            }),
        url(r'', include('django.contrib.staticfiles.urls')),
    )
