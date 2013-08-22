from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('example.urls')),
    # Examples:
    # url(r'^$', 'django_rest_model_hyperlink_serializers.views.home', name='home'),
    # url(r'^django_rest_model_hyperlink_serializers/', include('django_rest_model_hyperlink_serializers.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
    