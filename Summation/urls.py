from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Summation import views as vista

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Summation.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',vista.suma),
)

urlpatterns += staticfiles_urlpatterns()