#!/bin/sh

APP_PORT=${PORT:-8000}

gunicorn apps.backend.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:${APP_PORT} --log-level debug --reload
