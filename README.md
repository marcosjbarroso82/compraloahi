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



Folders to project:

compraloahi/
    apps/ ----------------------------> My django modules
    compraloahi/
        settings/ --------------------> Settings to django
    static/
        angular-resources/ -----------> Resources angular by site (less dashboard)
            app/ ---------------------> Individual app angular to one page
            modules/ -----------------> Angular modules to individual pages
        bower_components/ ------------> Third libraries to frontend install by bower
        css/ -------------------------> Custom style to all the site
        dashboard/ -------------------> Angular app and modules to dashboard
        image/ -----------------------> Folder to all static image by all site
        js/ --------------------------> My js script to sites
        templates-utils/ -------------> Utils template to site (ex. loading template)
        theme/ -----------------------> theme implemented on all site
    templates/
        dashboard/ -------------------> Layout to dashboard
        layout/ ----------------------> Layout to site