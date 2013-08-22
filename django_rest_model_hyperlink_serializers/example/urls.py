from django.views.generic import TemplateView
from django.conf.urls.defaults import patterns
from example import views
from rest_framework import routers
from django.conf.urls.defaults import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'team', views.TeamSet)
router.register(r'player', views.PlayerSet)


urlpatterns = patterns('', 
    (r'^$', TemplateView.as_view(template_name="index.html")),
    (r'^rest_api/', include(router.urls)),
)

urlpatterns += staticfiles_urlpatterns()
