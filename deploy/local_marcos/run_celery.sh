#!/bin/bash
ENVNAME=environment                                                   # Name of virtualenv
DJANGODIR=/webapps/compraloahi/compraloahi
USER=m                                                     # the user to run as
GROUP=m                                                                   # the group to run as
DJANGO_SETTINGS_MODULE=compraloahi.settings.settings               # which settings file should Django use

# Activate the virtual environment
cd $DJANGODIR
source ../$ENVNAME/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
      
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec celery -A compraloahi worker -l info


