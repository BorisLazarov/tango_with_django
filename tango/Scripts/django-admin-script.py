#!H:\tango\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Django==1.7.11','console_scripts','django-admin'
__requires__ = 'Django==1.7.11'
import sys
from pkg_resources import load_entry_point

sys.exit(
   load_entry_point('Django==1.7.11', 'console_scripts', 'django-admin')()
)
