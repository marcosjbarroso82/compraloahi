# Deploy Compraloahi

    # Download project
        git clone git@bitbucket.org:conmarcos/compraloahi.git
        cd compraloahi
        pip install -r requirements.txt

    # Install package Postman
	    hg clone http://bitbucket.org/psam/django-postman/ ~/.virtualenvs/env_compraloahi/lib/python3.4/site-packages/postman


Packages requeriments:
    # Added Support manipulation image with python
        sudo apt-get install libpng12-dev zlib1g-dev libfreetype6-dev libjpeg-dev
    # Requerments to haystack used spatial search
	    sudo apt-get install libgeos-dev