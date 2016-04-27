import os
import sys
from functools import wraps
from getpass import getpass, getuser
from glob import glob
from contextlib import contextmanager

from fabric.api import env, cd, prefix, sudo as _sudo, run as _run, hide, local, put, roles, warn_only
from fabric.contrib.files import exists, upload_template
from fabric.colors import yellow, green, blue, red
from fabric.contrib.console import confirm
from fabric.operations import prompt

from fabric.context_managers import settings


env.server_name = 'compraloahi.com.ar'
env.hosts =  ['162.243.201.32']
env.user = 'root'
env.user_path = '/webapps/compraloahi'
env.project_name = 'compraloahi'
env.db_name = 'db_%s' % env.project_name.lower()
env.db_password = 'TRuP9y8abxQ0SmsfdT3AM7gLVn4GFuMaYhPV1HfZolOoZEVAgPemIQlN4Gd0zvf'
env.project_path = '%s/%s' % (env.user_path, env.project_name)
env.application_path = '%s/%s/%s' % (env.user_path, env.project_name, env.project_name)
env.virtualenv_path = '%s/environment/bin/activate' % env.project_path
env.repository_type = 'git'
env.repository_url = 'git@bitbucket.org:contextdev/compraloahi.git'
env.manage = "%s/environment/bin/python %s/manage.py" % (env.user_path, env.application_path)

env.virtualenv_name = 'environment'
env.django_settings_modules = 'compraloahi.settings.production'
env.group = 'webapps'

env.web_user = env.project_name


REQUIRED_ENV_VAR = [
    'server_name',
]

from fabric.operations import require
def validate_required():
    """
    Check if the all required values exist on env object.
    """
    require(*REQUIRED_ENV_VAR)


templates = {
    'gunicorn' : {
         'local_path' : 'templates_config/gunicorn_start.sh',
         'remote_path' : '%s/bin' % env.project_path
    },
    'nginx' : {
        'local_path' : 'templates_config/nginx.conf',
        'remote_path' : '/etc/nginx/sites-enabled/%s.conf' % env.project_name,
        'reload_command' : 'service nginx restart'
    },
    "supervisor": {
        "local_path": "templates_config/supervisor.conf",
        "remote_path": "/etc/supervisor/conf.d/%s.conf" % env.project_name,
        "reload_command": "supervisorctl reload",
    }
}

SYSTEM_PACKAGES = [
    'gcc',
    'make',
    'git-core',
    'nginx', # Server
    'postgresql', # Database
    'postgresql-server-dev-all',
    'memcached',
    'libpng12-dev', # Required for work with images
    'zlib1g-dev', # Required for work with images
    'libfreetype6-dev', # Required for work with images
    'libjpeg-dev', # Required for work with images
    'openjdk-7-jre', # Required for elasticsearch

    #'libpq-dev', # Required for work width postgres

    'python3-all-dev', # All python lib to work

    # Required for some python libs
    'build-essential',
    'autoconf',
    'libtool',
    'pkg-config',
    'python-opengl',
    'python-imaging',
    'python-pyrex',
    'python-pyside.qtopengl',
    'libgle3',
    # END required for some python libs

    'python-setuptools',
    'libgeos-dev', # Required by gis
    'supervisor',
    'rabbitmq-server',
    'libxml2-dev'
]

def create_user(group=env.group, user=env.web_user):
    """
        Create user to manager deploy
    """
    #password = prompt("What is your password?") # TODO: This line is for test.
    with warn_only(): # TODO: warn_only equivalent to settings(warn_only=True):
        run('groupadd --system %s' % group)
        run('useradd --system --gid %s --shell /bin/bash --home %s %s' % (group, env.user_path, user))
        run('passwd %s' % user)




def swap():
    "List swap"
    run("swapon -s")


def swapon():
    "Add a Swap File"
    run("fallocate -l 1G /swapfile")
    run("ls -lh /swapfile")
    run("chmod 600 /swapfile")
    run("mkswap /swapfile")
    run("swapon /swapfile")
    run("free -m") # Check free space
    run("echo '# Paste this information at the bottom of the file' >> /etc/fstab")
    run("echo '/swapfile    none    swap    defaults    0   0' >> /etc/fstab")
    run("cat /proc/sys/vm/swappiness")
    run("cat /proc/sys/vm/vfs_cache_pressure")
    run("sysctl vm.vfs_cache_pressure=50")
    run("echo '# Search for the vm.swappiness setting.  Uncomment and change it as necessary.' >> /etc/sysctl.conf")
    run("echo 'vm.vfs_cache_pressure = 50' >> /etc/sysctl.conf")
    print(green("Swap ON"))



def _print(output):
    print(10*" ")
    print(output)
    print(10*" ")

def print_command(command):
    _print(blue("$ ", bold=True) +
           yellow(command, bold=True) +
           red(" ->", bold=True))

def run(command, show=True, *args, **kwargs):
    """
    Run a shell comand on the remote server.
    """
    if show:
        print_command(command)
    with hide("running"):
        return _run(command, *args, **kwargs)

def sudo(command, show=True, *args, **kwargs):
    """
    Run a command as sudo.
    """
    if show:
        print_command(command)
    with hide("running"):
        return _sudo(command, *args, **kwargs)

def psql(sql, show=True):
    """
    Executes a psql command
    """
    out = run('sudo -u postgres psql -c "%s"' % sql)
    if show:
       print_command(sql)
    return out

def pip(modules):
    """
    Install the Python modules passed as arguments with pip
    """
    with virtualenv():
        run('pip install %s' % modules)

def log_call(func):
    @wraps(func)
    def logged(*args, **kawrgs):
        header = "-" * len(func.__name__)
        _print(green("\n".join([header, func.__name__, header]), bold=True))
        return func(*args, **kawrgs)
    return logged

@contextmanager
def virtualenv():
    """
    Run commands within the project's virtualenv.
    """
    with prefix("source %s/%s/bin/activate" % (env.user_path, env.virtualenv_name)):
        yield


@contextmanager
def project():
    """
    Run commands within the project's directory.
    """
    with virtualenv():
        with cd(env.application_path):
            yield

def manage(command):
    """
    Run a Django management command.
    """
    return run("%s %s" % (env.manage, command))

@log_call
def generate_ssh_key():
    """
    Generates a key pair and displays the public key
    """
    with cd(env.user_path):
        sudo('ssh-keygen -t rsa', user=env.web_user)
        sudo('cat %s/.ssh/id_rsa.pub' % env.user_path, user=env.web_user)

@log_call
def install_aptitude():
    sudo('apt-get install aptitude -y')

@log_call
def upgrade():
    """
    Updates the repository definitions and upgrades the server
    """
    sudo('aptitude update -y')
    sudo('aptitude upgrade -y')

def upload_template_and_reload(name):
    template_settings = templates[name]
    local_path = template_settings['local_path']
    remote_path = template_settings['remote_path']
    reload_command = template_settings.get('reload_command')
    owner = template_settings.get("owner")
    mode = template_settings.get("mode")

    print('%s to %s' % (local_path, remote_path))

    upload_template(local_path, remote_path, env, use_sudo=True, backup=False)

    if owner:
        sudo("chown %s %s" % (owner, remote_path))
    if mode:
        sudo("chmod %s %s" % (mode, remote_path))

    if reload_command:
        sudo(reload_command)


@log_call
def install_base():
    """
    Installs the base software required to deploy an application
    """
    install_aptitude()
    sudo(
        "aptitude install {0} -y".format(' '.join(SYSTEM_PACKAGES))
    )

    sudo('add-apt-repository "deb http://packages.elasticsearch.org/elasticsearch/1.4/debian stable main"')
    sudo('apt-get update && sudo apt-get install elasticsearch')
    # Configure Elasticsearch to automatically start during bootup
    sudo('update-rc.d elasticsearch defaults 95 10')

    #run('wget http://www.ijg.org/files/jpegsrc.v8d.tar.gz')
    #run('tar xvzf jpegsrc.v8d.tar.gz')
    #with cd('jpeg-8d'):
    #    run('./configure')
    #    run('make')
    #    sudo('make install')

    #run('wget http://download.savannah.gnu.org/releases/freetype/freetype-2.4.10.tar.gz')
    #run('tar xvzf freetype-2.4.10.tar.gz')
    #with cd('freetype-2.4.10'):
    #    run('./configure')
    #    run('make')
    #    sudo('make install')

    #run('wget http://zlib.net/zlib-1.2.8.tar.gz')
    #run('tar xvzf zlib-1.2.8.tar.gz')
    #with cd('zlib-1.2.8'):
    #    run('./configure')
    #    run('make')
    #    sudo('make install')

    sudo('easy_install pip')
    sudo('pip install virtualenv mercurial')

    #run('echo -e "Host github.com\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config')
    #run('echo -e "Host bitbucket.org\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config')

    #sudo('rabbitmqctl add_user %s %s' % (env.project_name, env.db_name))
    #sudo('rabbitmqctl add_vhost %s' % env.project_name)
    #sudo(
    #    'rabbitmqctl set_permissions -p %s %s ".*" ".*" ".*"' %
    #    (env.project_name, env.project_name)
    #)

@log_call
def _create_database(name, password):
    psql("CREATE USER %s WITH ENCRYPTED PASSWORD '%s';" % (name, password))
    #psql("ALTER USER %s CREATEDB;" % name)
    psql("CREATE DATABASE %s WITH OWNER %s ENCODING='UTF8';" % (env.db_name, env.project_name))


@log_call
def create_database():
    """
    Creates a database and a database user with the project name and the specified password
    """
    _create_database(env.project_name, env.db_password)


@log_call
def create_folder_user():
    run('mkdir -p %s' % env.user_path)
    run('mkdir %s/logs' % env.user_path)
    change_own_folder_web_user()


def change_own_folder_web_user():
    run('chown %s:%s %s' % (env.web_user, env.group, env.user_path))

#@roles('compraloahi')
@log_call
def create():
    """
    Stages the application on the server
    """
    with cd(env.user_path):
        sudo('%s clone %s %s' %(env.repository_type, env.repository_url, env.project_name), user='compraloahi')

        run("virtualenv %s" % env.virtualenv_name)
        with virtualenv():
            #run('pip install -r %s/requirements/_base.txt' % env.project_path)
            run('pip install -r %s/requirements_dev.txt' % env.project_path)

    run('mkdir %s/bin' % env.project_path) # TODO THis line is patch because the folder bin doesnt exist on master branch
    upload_template_and_reload('gunicorn')
    upload_template_and_reload('nginx')
    upload_template_and_reload('supervisor')

    with virtualenv(), prefix('export DJANGO_SETTINGS_MODULE="%s"' % env.django_settings_modules):
        manage('migrate --all')
        manage("collectstatic -v 0 --noinput")

    change_own_folder_web_user()
    #if exists('%sgunicorn.pid'):
    #    sudo("kill -HUP 'cat %sgunicorn.pid'" % env.project_path)
    #else:
    run("supervisorctl start %s" % env.project_name)


@log_call
def install_all():
    install_aptitude()
    upgrade()
    install_base()
    create_user()
    create_folder_user()
    generate_ssh_key()
    confirm("Add this ssh key on repository and press ENTER to continue...", default=True)
    create_database()
    create()

@log_call
def create_superuser():
    with virtualenv():
        manage('createsuperuser')

def send_key():
    put('~/.ssh/id_rsa', '~/.ssh/id_rsa')
    put('~/.ssh/id_rsa.pub', '~/.ssh/id_rsa.pub')
    run('chmod 600 ~/.ssh/id_rsa')
    run('chmod 600 ~/.ssh/id_rsa.pub')