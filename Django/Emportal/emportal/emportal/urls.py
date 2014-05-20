from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'emportal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('emportal.views',
	(r'^emportal/$', 'hello'),
)

urlpatterns += patterns('serverips.views',
	(r'^emportal/servers/$', 'servers'),
)