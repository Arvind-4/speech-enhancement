#!/bin/sh

# uvicorn apps.backend.main:app --reload --host 0.0.0.0 --port 8000
python apps/backend/manage.py runserver