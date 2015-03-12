#!/usr/bin/python3
import os
import sys


print(len(sys.argv))
if len(sys.argv) > 1:
    arguments = sys.argv[1]
    if len(sys.argv) > 2:
        arguments = ''
        for arg in sys.argv[1:]:
            arguments = arguments + " " + arg

    os.system("python manage.py "+ arguments +" --settings=compraloahi.settings.local")
else:
    print("Need parameter. Ex. runserver, shell, shell_plus, ")
