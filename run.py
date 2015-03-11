#!/usr/bin/python3
import os
import sys


print(len(sys.argv))
if len(sys.argv) > 1:
    os.system("python manage.py "+ sys.argv[1] +" --settings=compraloahi.settings.local")
else:
    print("Need parameter. Ex. runserver, shell, shell_plus, ")
