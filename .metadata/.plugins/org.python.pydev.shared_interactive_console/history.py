import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'djangobasic.settings'; import django
if django.get_version() < '1.5':
    from django.core import management
    import djangobasic.settings as settings
    management.setup_environ(settings)
if django.get_version() >= '1.7':
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
from book.models import Publishers
import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'djangobasic.settings'; import django
if django.get_version() < '1.5':
    from django.core import management
    import djangobasic.settings as settings
    management.setup_environ(settings)
if django.get_version() >= '1.7':
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
manage.py sqlmigrate books 0001
import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'djangobasic.settings'; import django
if django.get_version() < '1.5':
    from django.core import management
    import djangobasic.settings as settings
    management.setup_environ(settings)
if django.get_version() >= '1.7':
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
python manage.py shell
