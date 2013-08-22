import os,sys
import site
site.addsitedir('/home/ubuntu/.virtualenvs/{{ project_name }}/lib/python2.7/site-packages')
apache_configuration = os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)
sys.path.append('/home/ubuntu/{{ project_name }}_project/{{ project_name }}')

os.environ['DJANGO_SETTINGS_MODULE'] = '{{ project_name }}.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
