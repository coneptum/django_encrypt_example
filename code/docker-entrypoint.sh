#!/bin/bash
#sleep 60000
python manage.py mamkemigrations --merge
python manage.py migrate
python manage.py runserver 0.0.0.0:8000