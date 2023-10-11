#!/bin/bash
python manage.py collectstatic --noinput
gunicorn -b 0.0.0.0:8000 afetweb.asgi:application --preload -w 2 -k uvicorn.workers.UvicornWorker