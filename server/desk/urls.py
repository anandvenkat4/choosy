from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('desk.views',
    url(r'^$', 'index', name='desk'),
    url(r'^new/$', 'edit', name='new_exercise'),
    url(r'^import/$', 'import_', name='import_exercise'),
    url(r'^(?P<exid>\d+)/$', 'show', name='desk_show_exercise'),
    url(r'^(?P<exid>\d+)/edit/$', 'edit', name='edit_exercise'),
    url(r'^(?P<exid>\d+)/delete/$', 'delete', name='delete_exercise'),
    url(r'^(?P<exid>\d+)/yaml/$', 'yaml', name='yaml_exercise'),
)
