#!/bin/bash

export EDO_SETTINGS=/lain/app/local_settings.py
mkdir -p /lain/logs
exec gunicorn -c gunicorn.conf.py edo:app
