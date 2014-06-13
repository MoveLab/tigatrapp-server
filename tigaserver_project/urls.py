from django.conf.urls import *
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from tigahelp.views import show_help, show_about, show_license, show_policies, show_terms, show_privacy, \
    show_credit_image
from tigamap import views

admin.autodiscover()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('tigaserver_app.urls')),
    url(r'^webapp/', include('webapp.urls')),
    url(r'^help/(?P<platform>\w+)/(?P<language>\w+)/$', show_help),
    url(r'^about/(?P<platform>\w+)/(?P<language>\w+)/$', show_about),
    url(r'^credits/$', show_credit_image, name='show_credit_image'),
    url(r'^license/(?P<platform>\w+)/(?P<language>\w+)/$', show_license),
    (r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^webmap/embedded/ca/$', RedirectView.as_view(url='/ca/webmap/embedded/', permanent=False)),
    url(r'^webmap/embedded/es/$', RedirectView.as_view(url='/es/webmap/embedded/', permanent=False)),
    url(r'^webmap/embedded/en/$', RedirectView.as_view(url='/en/webmap/embedded/', permanent=False)),
    url(r'^webmap/ca/$', RedirectView.as_view(url='/ca/webmap/', permanent=False)),
    url(r'^webmap/es/$', RedirectView.as_view(url='/es/webmap/', permanent=False)),
    url(r'^webmap/en/$', RedirectView.as_view(url='/en/webmap/', permanent=False)),
    url(r'^policies/es/$', RedirectView.as_view(url='/es/policies/', permanent=False)),
    url(r'^policies/ca/$', RedirectView.as_view(url='/ca/policies/', permanent=False)),
    url(r'^policies/en/$', RedirectView.as_view(url='/en/policies/', permanent=False)),
    url(r'^terms/es/$', RedirectView.as_view(url='/es/terms/', permanent=False)),
    url(r'^terms/ca/$', RedirectView.as_view(url='/ca/terms/', permanent=False)),
    url(r'^terms/en/$', RedirectView.as_view(url='/en/terms/', permanent=False)),
    url(r'^privacy/es/$', RedirectView.as_view(url='/es/privacy/', permanent=False)),
    url(r'^privacy/ca/$', RedirectView.as_view(url='/ca/privacy/', permanent=False)),
    url(r'^privacy/en/$', RedirectView.as_view(url='/en/privacy/', permanent=False)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                             document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns('',
    url(r'^policies/$', show_policies, name='help.show_policies'),
    url(r'^terms/$', show_terms, name='help.show_terms'),
    url(r'^privacy/$', show_privacy, name='help.show_privacy'),
    url(r'^webmap/embedded/$', views.show_embedded_webmap),
    url(r'^webmap/testingzone/(?P<report_type>\w+)/(?P<category>\w+)/$', views.show_map, {'data': 'beta'}),
    url(r'^webmap/testingzone/(?P<report_type>\w+)/$', views.show_map, {'data': 'beta'}),
    url(r'^webmap/testingzone/$', views.show_map, {'data': 'beta'}),
    url(r'^betamap/(?P<report_type>\w+)/(?P<category>\w+)/$', views.show_map, {'data': 'beta'}, name='webmap'
                                                                                                '.show_map_beta'),
    url(r'^betamap/(?P<report_type>\w+)/$', views.show_map, {'data': 'beta'}),
    url(r'^betamap/$', views.show_map, {'data': 'beta'}),
    url(r'^webmap/(?P<report_type>\w+)/(?P<category>\w+)/$', views.show_map, name='webmap.show_map'),
    url(r'^webmap/(?P<report_type>\w+)/$', views.show_map),
    url(r'^webmap/$', views.show_map),
    url(r'^$', views.show_map),
)
