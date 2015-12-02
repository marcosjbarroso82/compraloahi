#!/bin/bash
ENVNAME=enviroment                                                   # Name of virtualenv
DJANGODIR=/webapps/owncommerce/owncommerce
USER=owncommerce                                                                # the user to run as
DJANGO_SETTINGS_MODULE=owncommerce.settings.custom                    # which settings file should Django use

# Activate the virtual environment
cd $DJANGODIR
source ../$ENVNAME/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
      
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec celery -A owncommerce beat

