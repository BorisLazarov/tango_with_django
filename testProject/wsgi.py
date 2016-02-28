"""
WSGI config for testProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testProject.settings")
os.environ['HTTPS'] = "on"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


def build_absolute_uri(self, location=None):
    """
    Builds an absolute URI from the location and the variables available in
    this request. If no location is specified, the absolute URI is built on
    ``request.get_full_path()``.
    """
    if not location:
        location = self.get_full_path()
    if not absolute_http_url_re.match(location):
        current_uri = '%s://%s%s' % (self.is_secure() and 'https' or 'http',
                                     self.get_host(), self.path)
        location = urljoin(current_uri, location)
    return iri_to_uri(location)

def is_secure(self):
    return os.environ.get("HTTPS") == "on"