{% if False %}


Django Grunt Template
========================

This template creates django project with grunt.js integration, Grunt will
be watching changes during development and run tasks paralell with the
development server.

Grunt tasks for deployment are already made, this will also clean up any
source files.


ToDo
------------------------

- Create a deployment fabfile.


Installation
------------------------

To start a new project with this template::

	django-admin.py startproject <project_name> --template=https://github.com/mikedingjan/django-grunt-template/zipball/master --extension=py,js,json,gitignore,wsgi,conf,md,html <destination>

{% endif %}


{{ project_name|title }}
========================

Below you'll find a basic setup instructions for the {{ project_name }} project.
To begin you should have the following applications installed on you local
development system::

- git >= 1.7
- node.js >= 1.2
- Postgres >= 8.4
- Python >= 2.7
- `pip >= 1.1 <http://www.pip-installer.org/>`
- `virtualenv >= 1.8 <http://www.virtualenv.org/>`
- `virtualenvwrapper >= 3.0 <http://pypi.python.org/pypi/virtualenvwrapper>`


Getting started
------------------------

To setup you local environment you should create a virtualenv and install the
necessary requirements:

	mkvirtualenv {{ project_name }}
	$VIRTUAL_ENV/bin/pip install -r $PWD/requirements/requirements.txt
	npm install

Then create a local settings file and edit this according your needs::

	cp {{ project_name }}/settings/local_example.py {{ project_name }}/settings/local.py

Create the Postgres database and run the initial syncdb/migrate::

	createdb -E UTF-8 {{ project_name }}
	python manage.py syncdb
	python manage.py migrate

You can now use the development server::

	python manange.py runserver --grunt
