#!/usr/bin/env bash
sleep 20


echo "[run] Celery worker"
celery -A compraloahi worker -l info

echo "[run] Celery Beat"
celery -A compraloahi beat || exit 1



