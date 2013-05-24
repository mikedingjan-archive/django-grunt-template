import sys
import logging

from {{ project_name }}.settings.base import *

try:
    from {{ project_name }}.settings.local import *
except ImportError:
    logging.basicConfig(level=logging.WARNING, stream=sys.stderr)
