# compraloahi
Compraloahi es un portal de anuncios centrado en la ubicacion y la interaccion con mapas. Aqui puedes ver unas demostracions:

[Video presentacion](https://drive.google.com/open?id=0BySTS6ddk66XcGtNRC1MX2ZfdkE "title" target="_blank")  
[Video Demo de Uso](https://drive.google.com/open?id=0BySTS6ddk66XWGxsN0pVVUtrV2s "title" target="_blank")  
[Video Demo Admin](https://drive.google.com/open?id=0BySTS6ddk66XSlRtQUdxRDdxVkU "title" target="_blank")  

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
            theme/ -------------------> Css theme implement
            less/ --------------------> Custom style with less
        dashboard/ -------------------> Angular app and modules to dashboard
        image/ -----------------------> Folder to all static image by all site
        js/ --------------------------> My js script to sites
            theme/ -------------------> Js theme
        templates-utils/ -------------> Utils template to site (ex. loading template)

    templates/
        dashboard/ -------------------> Layout to dashboard
        layout/ ----------------------> Layout to site




Soluciones al actualizar django 1.8

Packages update:
   pip install --upgrade django
   pip install django-taggit --upgrade
   pip install django-debug-toolbar --upgrade
   pip install git+https://github.com/django/django-contrib-comments
   pip install git+https://github.com/danirus/django-comments-xtd.git

Run migrate:
 manage.py migrate sites
 manage.py migrate auth
 manage.py migrate

Compilar archivos minimificados

Instalar:
npm install --save gulp-concat-css
npm install --save gulp-minify-css
npm install --save gulp-concat
npm install --save gulp-notify
npm install --save gulp-uglify

Correr:
gulp js-dashboard-app
