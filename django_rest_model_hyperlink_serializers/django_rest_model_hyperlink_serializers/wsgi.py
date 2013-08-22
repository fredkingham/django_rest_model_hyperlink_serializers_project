"""
WSGI config for fredkingham_site project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import sys
import site
from os.path import basename, dirname
from os import environ


# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.

site.addsitedir('/home/ubuntu/.virtualenvs/django_rest_model_hyperlink_serializers/lib/python2.7/site-packages')
sys.path.append('/home/ubuntu/fredkingham_site_project/django_rest_model_hyperlink_serializers')
settings_module = basename(dirname(__file__)) + '.settings'
environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
