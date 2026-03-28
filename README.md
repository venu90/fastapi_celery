# FastAPI + Celery + Redis Demo

## Features
- Background task processing using Celery
- Redis as broker and cache
- FastAPI endpoints

## Endpoints
- GET /add?x=1&y=2
- GET /result/{task_id}
- GET /cached/{key}

## Run

Start Redis:
redis-server

or 
docker run -d -p 6379:6379 redis

Start API:
uvicorn app:app --reload

Start Worker:
celery -A app.celery_app worker --pool=solo --loglevel=info