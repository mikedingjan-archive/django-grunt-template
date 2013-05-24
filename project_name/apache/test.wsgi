import os, site, sys

# Calculate the path based on the location of the WSGI script.
apache_configuration = os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)

old_sys_path_items = list(sys.path)

virtual_env_dir = '/var/virtualenv/{{ project_name }}/lib/python2.7/site-packages'
site.addsitedir(virtual_env_dir)

sys.path.append(project)

new_sys_path_items = set(sys.path) - set(old_sys_path_items)
sys.path = list(new_sys_path_items) + old_sys_path_items

os.environ['DJANGO_SETTINGS_MODULE'] = '{{ project_name }}.settings.env.test'
try:
    from {{ project_name }}.wsgi import application
except:
    pass
