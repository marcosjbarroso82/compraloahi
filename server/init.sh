#!/usr/bin/env bash
sleep 20

echo "[run] make migrations"
python3 manage.py makemigrations || exit 1

echo "[run] Migrate DB"
python3 manage.py migrate || exit 1

echo "[run] Collect static files"
python3 manage.py collectstatic --noinput

echo "[run] Create superuser"
echo "from django.contrib.auth.models import User
from apps.interest_group.models import InterestGroup
from apps.ad.models import Category
if not User.objects.filter(username='admin').count():
    user = User.objects.create_superuser('admin', 'contextinformatic@gmail.com', 'qwerty123')
    ig = InterestGroup()
    ig.name = 'public'
    ig.short_description = 'grupo publico'
    ig.description = 'grupo publico'
    ig.owner = user
    ig.save()
    cat = Category()
    cat.name = 'Test'
    cat.color = '#c4c2c2'
    cat.save()

" | python3 manage.py shell || exit 1

#echo "[run] runserver"
/usr/local/bin/gunicorn compraloahi.wsgi:application -w 2 -b :8000 --reload
